import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.parametrize("admin_user,admin_pass,new_user,new_pass", [
    ("Admin", "admin123", "newtestuser01", "User@1234")
])
def test_create_user_and_login(driver, admin_user, admin_pass, new_user, new_pass):
    wait = WebDriverWait(driver, 10)

    # Step 1: Admin login
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(admin_user)
    driver.find_element(By.NAME, "password").send_keys(admin_pass)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    # Step 2: Navigate to Admin > User Management > Users
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Admin']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Add']"))).click()

    # Step 3: Fill the user creation form
    # User Role
    wait.until(EC.element_to_be_clickable((By.XPATH, "//label[text()='User Role']/../following-sibling::div"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='ESS']"))).click()

    # Employee Name
    emp_name_input = driver.find_element(By.XPATH, "//input[@placeholder='Type for hints...']")
    emp_name_input.send_keys("Kani")
    wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@role='listbox']//span"))).click()

    # Username
    driver.find_element(By.XPATH, "//label[text()='Username']/../following-sibling::div/input").send_keys(new_user)

    # Status
    driver.find_element(By.XPATH, "//label[text()='Status']/../following-sibling::div").click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Enabled']"))).click()

    # Password
    driver.find_element(By.XPATH, "//label[text()='Password']/../following-sibling::div/input").send_keys(new_pass)

    # Confirm Password
    driver.find_element(By.XPATH, "//label[text()='Confirm Password']/../following-sibling::div/input").send_keys(new_pass)

    # Save
    driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()

    # Wait until user is saved (back to user list)
    wait.until(EC.presence_of_element_located((By.XPATH, "//h6[text()='System Users']")))

    # Step 4: Logout
    driver.find_element(By.CLASS_NAME, "oxd-userdropdown-tab").click()
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Logout"))).click()

    # Step 5: Login as new user
    wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(new_user)
    driver.find_element(By.NAME, "password").send_keys(new_pass)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    # Step 6: Verify login
    assert "dashboard" in driver.current_url.lower()
