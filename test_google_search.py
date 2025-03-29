import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller

@pytest.fixture(scope="module")
def driver():
    # Ensure ChromeDriver is installed
    chromedriver_autoinstaller.install()

    # Set up Chrome options
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36")

    # Start WebDriver
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_google_search(driver):
    driver.get("https://www.google.com")

    # Wait for search box to appear
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    search_box.send_keys("Selenium with PyTest")
    search_box.send_keys(Keys.RETURN)

    # ✅ Wait until search results load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "h3"))
    )

    results = driver.find_elements(By.CSS_SELECTOR, "h3")
    assert len(results) > 0, "No search results found!"
