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
    # Install and setup ChromeDriver automatically
    chromedriver_autoinstaller.install()
    
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")  
    chrome_options.add_argument("--disable-dev-shm-usage")  
    chrome_options.add_argument("--headless")  
    chrome_options.add_argument(f"--user-data-dir=/tmp/chrome-user-{os.getpid()}")  

    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()

def test_google_search(driver):
    driver.get("https://www.google.com")

    # Wait for the search box to be present
    wait = WebDriverWait(driver, 10)  
    search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))
    
    search_box.send_keys("Selenium with PyTest")
    search_box.send_keys(Keys.RETURN)

    # Wait for search results to load
    results = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "h3")))

    assert len(results) > 0, "No search results found!"
