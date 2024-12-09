import requests
import os

def fetch_zoho_data():
    """
    Fetch leads from Zoho API.

    Returns:
        list: A list of leads fetched from Zoho.
    """
    # Get the access token using client ID and client secret
    access_token = get_access_token()
    
    url = "https://www.zohoapis.com/crm/v2/Leads"  # Example endpoint for leads
    headers = {
        "Authorization": f"Zoho-oauthtoken {access_token}",  # Use the environment variable
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        leads = response.json().get('data', [])
        return leads
    else:
        print(f"Error fetching data: {response.status_code} - {response.text}")
        return []

def get_access_token():
    """
    Get the access token from Zoho using client ID and client secret.

    Returns:
        str: The access token.
    """
    url = "https://accounts.zoho.com/oauth/v2/token"
    params = {
        "grant_type": "client_credentials",
        "client_id": os.getenv("ZOHO_CLIENT_ID"),
        "client_secret": os.getenv("ZOHO_CLIENT_SECRET"),
        "scope": "ZohoCRM.modules.ALL"
    }
    response = requests.post(url, params=params)
    if response.status_code == 200:
        return response.json().get("access_token")
    else:
        print(f"Error fetching access token: {response.status_code} - {response.text}")
        return None 