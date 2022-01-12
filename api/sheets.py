import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
# stands for pretty print


def write_ghseets():
    scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

    creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

    client = gspread.authorize(creds)

    sheet = client.open("isaa").sheet1

    data = sheet.get_all_records()

    # to insert an entire row
    logRow = [2, 2, 'aa', 'asfgag']
    sheet.insert_row(logRow)

    pprint(data)

