import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.parametrize("admin_user, admin_pass, expected_user", [
    ("Admin", "admin123", "newtestuser01")
])
def test_user_exists_in_admin_menu(driver, admin_user, admin_pass, expected_user):
    wait = WebDriverWait(driver, 15)

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    print("Opened login page.")

    # Log in
    wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(admin_user)
    driver.find_element(By.NAME, "password").send_keys(admin_pass)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    print("Login submitted.")

    # Confirm dashboard is loaded
    wait.until(EC.presence_of_element_located((By.XPATH, "//h6[text()='Dashboard']")))
    print("Login successful and dashboard visible.")

    # Navigate to Admin tab
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Admin']"))).click()
    print("Navigated to Admin menu.")

    # Search for the user
    username_input_xpath = "//label[text()='Username']/../following-sibling::div/input"
    wait.until(EC.presence_of_element_located((By.XPATH, username_input_xpath))).send_keys(expected_user)

    driver.find_element(By.XPATH, "//button[normalize-space()='Search']").click()
    print(f"Searching for user: {expected_user}")

    # Verify user appears in the search result
    result_xpath = f"//div[@role='row']//div[text()='{expected_user}']"
    wait.until(EC.visibility_of_element_located((By.XPATH, result_xpath)))
    assert driver.find_element(By.XPATH, result_xpath).is_displayed()
    print(f"User {expected_user} found in Admin list.")
