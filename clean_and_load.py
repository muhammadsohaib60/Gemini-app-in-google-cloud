import gspread
from oauth2client.service_account import ServiceAccountCredentials
import requests

def clean_and_load(sheet_url):
    """
    Cleans the Google Sheet by removing rows with high open rates and creates leads in Zoho CRM.

    Parameters:
        sheet_url (str): The URL of the Google Sheet containing email data.
    """
    # Set up the Google Sheets API
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name('path/to/your/credentials.json', scope)
    client = gspread.authorize(creds)

    # Open the Google Sheet
    sheet = client.open_by_url(sheet_url).sheet1

    # Check for high open rates and clean the sheet
    for i in range(2, sheet.row_count + 1):  # Assuming the first row is headers
        open_rate = sheet.cell(i, 5).value  # Assuming open rate is in the 5th column
        if int(open_rate) > 5:
            sheet.delete_row(i)
            print(f"Deleted row {i} due to high open rate.")

    # Create leads in Zoho CRM
    create_leads_in_zoho(sheet)

def create_leads_in_zoho(sheet):
    """
    Creates leads in Zoho CRM based on the data in the Google Sheet.

    Parameters:
        sheet: The Google Sheet object containing email data.
    """
    for i in range(2, sheet.row_count + 1):  # Assuming the first row is headers
        row = sheet.row_values(i)
        lead_data = {
            "data": [
                {
                    "First_Name": row[0],
                    "Last_Name": row[1],
                    "Email": row[3],
                    "Hospital": row[2],
                    # Add other fields as necessary
                }
            ]
        }
        url = "https://www.zohoapis.com/crm/v2/Leads"
        headers = {
            "Authorization": "Zoho-oauthtoken YOUR_ACCESS_TOKEN",  # Replace with your token
            "Content-Type": "application/json"
        }
        response = requests.post(url, json=lead_data, headers=headers)
        if response.status_code == 201:
            print(f"Lead created for {row[0]} {row[1]}")
        else:
            print(f"Error creating lead: {response.status_code} - {response.text}") 