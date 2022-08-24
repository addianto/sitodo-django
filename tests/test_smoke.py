from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os


class UISmokeTest(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        options: Options = Options()

        if _is_running_on_ci():
            options.headless = True
            options.add_argument("no-sandbox")

        cls.selenium: WebDriver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )
        cls.selenium.implicitly_wait(5)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_title(self):
        self.selenium.get(self.live_server_url)

        self.assertIn("SITODO", self.selenium.title)


def _is_running_on_ci() -> bool:
    _CI: str = os.getenv("CI", "false")

    return True if _CI == "true" else False
