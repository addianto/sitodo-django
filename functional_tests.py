from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.get("http://localhost:8000")

logo: WebElement = browser.find_element(By.CLASS_NAME, "logo")

assert "Congratulations!" in browser.title
assert "django" in logo.text

browser.quit()

# TODO Create a unittest-based test script
