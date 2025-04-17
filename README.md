# PAT_webcode_2

OrangeHRM Login Automation Project
Automated testing project for OrangeHRM using Selenium, Pytest, Page Object Model (POM), and Data-Driven Testing (DDTF) with Excel input. This framework also generates HTML test reports using Pytest plugins.

Features
1. Login verification using multiple credentials from Excel

2. Cookie-based login validation

3. UI element visibility checks (username/password fields)

4. Dashboard menu validations

5. User creation and verification in Admin panel

6. Fully structured with Page Object Model

7. Generates Pytest-based HTML reports

8. Handles exceptions and timeouts gracefully

9. Clean project structure using OOP and modular design

Project Structure
project/
│
|-- data/
│   --- testdata.xlsx          # Excel file for login/user test data
│
|-- pages/
│   --- base_page.py           # Common methods for all pages
│   --- login_page.py          # Login page actions
│   --- dashboard_page.py      # Dashboard/menu page actions
│   --- admin_page.py          # Admin/user search and creation
│
|-- tests/
│   --- test_login_ddtf.py     # Login with Excel data (Test-Case-1)
│   --- test_home_url.py       # Home URL check (Test-Case-2)
│   --- test_login_fields.py   # Field visibility (Test-Case-3)
│   --- test_dashboard_menus.py# Menu clickability (Test-Case-4)
│   --- test_create_user.py    # User creation (Test-Case-5)
│   --- test_verify_user_exists.py # Verify created user (Test-Case-6)
│
|-- utils/
│   --- excel_reader.py        # Utility to read Excel test data
│   --- config.py              # URL, credentials, settings
│
|-- conftest.py                # Pytest setup, browser fixture
|-- requirements.txt           # Required Python packages
|-- README.md                  # Project overview

Test Cases Covered
Test-Case-1 
Data-driven login test using Excel data
Test-Case-2
Home URL availability check
Test-Case-3 
Username and password field visibility
Test-Case-4 
Menu visibility after login (Admin, PIM, etc.)
Test-Case-5 
Create new user from Admin panel
Test-Case-6 
Verify user exists in Admin panel

Tools used
1. Python
2. Selenium WebDriver
3. Pytest
4. OpenPyXL (for Excel read/write)
5. HTML Test Report via pytest-html
6. Page Object Model
7. OrangeHRM (open-source demo site)

Run all tests and generate HTML report
pytest --html=reports/report.html --self-contained-html

Run an individual test:
pytest tests/test_login_ddtf.py --html=reports/login_report.html

Best Practices Followed
1. Python OOP and modular design
2. Exception Handling and logging
3. Explicit waits (no time.sleep)
4. Fully structured Page Object Model
5. Clean, scalable code for real-world teams

THIS PROJECT IS COMPLETED BY KANISHKA S
