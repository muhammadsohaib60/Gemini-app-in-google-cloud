from src.email_sender import send_emails

def automate_user_sends(sheet_url, number_of_sends):
    """
    Automates the sending of emails from multiple Google accounts.

    Parameters:
        sheet_url (str): The URL of the Google Sheet containing email data.
        number_of_sends (int): The number of emails to send.
    """
    # Example: Send emails from different accounts
    for account in range(1, 21):  # Assuming 20 accounts
        print(f"Logging in to account {account}...")
        start_row = (account - 1) * number_of_sends + 1
        send_emails(sheet_url, start_row, number_of_sends) 