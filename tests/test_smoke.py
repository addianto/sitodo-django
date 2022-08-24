from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.chrome.service import Service
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

        cls.selenium: WebDriver = webdriver.Chrome(
            options=options, service=Service(ChromeDriverManager().install())
        )
        cls.selenium.implicitly_wait(5)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_title(self) -> None:
        self.selenium.get(self.live_server_url)

        self.assertIn("SITODO", self.selenium.title)


def _is_running_on_ci() -> bool:
    _CI: str = os.getenv("CI", "false")

    return True if _CI == "true" else False
