# Import Selenium WebDriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Specify the path to the ChromeDriver
# If ChromeDriver is not in your system PATH, provide the exact path to the driver

url = "https://www.google.com"

# Open Google
driver = webdriver.Chrome()
driver.get(url)

# Locate the search input field using its name attribute and type "Instagram"
search_box = driver.find_element(By.NAME, "q")  # Google's search box typically has the name "q"
search_box.send_keys("Instagram")

# Simulate hitting the Enter key
search_box.send_keys(Keys.RETURN)


# Print the title of the current webpage
print("Page Title is: ", driver.title)

# Close the browser
driver.quit()
