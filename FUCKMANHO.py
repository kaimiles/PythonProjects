"""
Google Sheets Bot (Google Sheets API - no credentials needed for public sheets)
--------------------------------------------------------------------------------
Checks if cells G11:K11 are filled in a public Google Sheet.
If not, fills them with the specified values. Rechecks every 60 seconds.

Requirements:
    pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client

Setup:
    1. Go to https://console.cloud.google.com/
    2. Create a new project (or select an existing one)
    3. Enable the "Google Sheets API"
    4. Go to "APIs & Services" > "Credentials"
    5. Click "Create Credentials" > "Service Account"
    6. Give it any name, click Done
    7. Click the service account > "Keys" tab > "Add Key" > "JSON"
    8. Save the downloaded file as "service_account.json" in the same folder as this script
    9. Share the Google Sheet with the service account email (found in the JSON as "client_email")
       and give it "Editor" access
"""

import time
from datetime import datetime
from google.oauth2 import service_account
from googleapiclient.discovery import build

# --- Configuration ---
SPREADSHEET_ID = "1Lk_yc4KfAMwA1NEk2cRaXLrcZAWqx_zukVh3zdlVD48"
SHEET_NAME = "Sheet1"  # Change if your tab has a different name
RANGE = f"{SHEET_NAME}!G11:K11"

VALUES_TO_FILL = [
    "A870035554",              # G11
    "British",                 # H11
    "886 916433176",           # I11
    "台北市中山區敬業一路135號",   # J11
    "kaimiles@hotmail.com.hk"  # K11
]

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
SERVICE_ACCOUNT_FILE = "service_account.json"


def get_service():
    """Authenticate using service account and return Sheets service."""
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES
    )
    return build("sheets", "v4", credentials=creds)


def check_and_fill(service):
    """Check G11:K11 and fill any empty cells."""
    sheet = service.spreadsheets()

    result = sheet.values().get(
        spreadsheetId=SPREADSHEET_ID,
        range=RANGE
    ).execute()

    existing = result.get("values", [[]])[0] if result.get("values") else []
    existing += [""] * (5 - len(existing))  # Pad to 5 elements

    labels = ["G11", "H11", "I11", "J11", "K11"]

    all_filled = all(v.strip() for v in existing)
    if all_filled:
        print("  ✅ All cells G11:K11 are filled. No changes needed.")
        return

    for label, val in zip(labels, existing):
        if not val.strip():
            print(f"  ⚠️  {label} is empty — will be filled.")
        else:
            print(f"  ✅ {label} = '{val}'")

    body = {"values": [VALUES_TO_FILL]}
    sheet.values().update(
        spreadsheetId=SPREADSHEET_ID,
        range=RANGE,
        valueInputOption="RAW",
        body=body
    ).execute()

    print("  ✍️  Cells filled:")
    for label, val in zip(labels, VALUES_TO_FILL):
        print(f"      {label} → '{val}'")


def main():
    print("🔑 Connecting to Google Sheets API...")
    service = get_service()
    print("  Connected.\n")

    print("🤖 Bot running — rechecking every 60 seconds. Press Ctrl+C to stop.\n")
    while True:
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Running check...")
        try:
            check_and_fill(service)
        except Exception as e:
            print(f"  ❌ Error: {e}")
        print("⏳ Waiting 60 seconds...\n")
        time.sleep(60)


if __name__ == "__main__":
    main()