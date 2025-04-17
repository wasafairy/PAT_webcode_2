import pytest

def test_home_url(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    assert "orangehrmlive" in driver.current_url, "Home URL did not load properly"
