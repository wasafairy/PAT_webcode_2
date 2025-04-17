import openpyxl

def get_login_data(filepath):
    workbook = openpyxl.load_workbook(filepath)
    sheet = workbook.active

    data = []
    for row in sheet.iter_rows(min_row=2, values_only=True):  # skip header row
        if row and row[0] and row[1]:  # make sure at least 2 values are present
            username = row[0]
            password = row[1]
            data.append((username, password))  # ignore extra columns
    return data
