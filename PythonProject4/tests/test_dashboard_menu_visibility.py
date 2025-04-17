import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

menu_items = [
    "Admin",
    "PIM",
    "Leave",
    "Time",
    "Recruitment",
    "My Info",
    "Performance",
    "Dashboard"
]

@pytest.mark.parametrize("username,password", [("Admin", "admin123")]) 
def test_menu_items_after_login(driver, username, password):
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Login
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    # Wait for Dashboard page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "oxd-topbar-header-breadcrumb")))

    # Check each menu item
    for item in menu_items:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//span[text()='{item}']"))
        )
        assert element.is_displayed(), f"{item} menu is not visible"
        assert element.is_enabled(), f"{item} menu is not clickable"
