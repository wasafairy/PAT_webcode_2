import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_input_fields_visibility(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Wait and check if username field is visible
    username_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "username"))
    )
    assert username_field.is_displayed(), "Username input box is not visible"

    # Wait and check if password field is visible
    password_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "password"))
    )
    assert password_field.is_displayed(), "Password input box is not visible"
