import pytest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller

@pytest.fixture(scope="function")
def driver():
    chromedriver_autoinstaller.install()  # Automatically installs ChromeDriver

    # Set Chrome options to use a fresh profile and avoid session issues
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")  # Required for GitHub Actions
    chrome_options.add_argument("--disable-dev-shm-usage")  # Fixes crashes in some environments
    chrome_options.add_argument("--headless")  # Runs in headless mode (no UI)
    chrome_options.add_argument(f"--user-data-dir=/tmp/chrome-user-{os.getpid()}")  # Unique profile

    driver = webdriver.Chrome(options=chrome_options)
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
