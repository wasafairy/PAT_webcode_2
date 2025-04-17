import openpyxl

def read_login_data(file_path, sheet_name):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook[sheet_name]
    data = []

    for row in sheet.iter_rows(min_row=2, values_only=True):
        # This will only take first two columns: username and password
        username = row[0]
        password = row[1]
        if username and password:
            data.append((username, password))

    return data
