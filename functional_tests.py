from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.firefox import GeckoDriverManager
import selenium.webdriver.common as Common

browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
browser.get('http://localhost:8000')

logo: WebElement = browser.find_element(By.CLASS_NAME, 'logo')

assert 'Congratulations!' in browser.title
assert 'django' in logo.text

browser.quit()

# TODO Create a unittest-based test script
