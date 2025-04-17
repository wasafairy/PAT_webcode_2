import sys
import os
import pytest

# Ensure the parent directory is in the path so we can import from utils and pages
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.read_excel import get_login_data
from pages.login_page import LoginPage

# Updated path for Excel directly in root directory
excel_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'ORANGE.xlsx'))

@pytest.mark.parametrize("username,password", get_login_data(excel_file))
def test_login_logout(driver, username, password):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()

    assert login_page.is_login_successful(), f"Login failed for {username}"
    login_page.logout()
