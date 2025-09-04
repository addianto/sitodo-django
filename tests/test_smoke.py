from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import WebDriverException
import os
import tempfile
import shutil


class UISmokeTest(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        options: Options = Options()

        if _is_running_on_ci():
            options.headless = True

        cls.user_data_dir = tempfile.mkdtemp()
        options.add_argument(f"--user-data-dir={cls.user_data_dir}")

        try:
            cls.selenium: WebDriver = webdriver.Chrome(
                options=options, service=ChromeService(ChromeDriverManager().install())
            )
        except WebDriverException:
            cls.selenium = webdriver.Chrome(
                options=options,
                service=ChromeService(
                    ChromeDriverManager(chrome_type="chromium").install()
                ),
            )

        cls.selenium.implicitly_wait(5)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()

        if os.path.exists(cls.user_data_dir):
            shutil.rmtree(cls.user_data_dir, ignore_errors=True)

        super().tearDownClass()

    def test_title(self) -> None:
        self.selenium.get(self.live_server_url)

        self.assertIn("SITODO", self.selenium.title)


def _is_running_on_ci() -> bool:
    _CI: str = os.getenv("CI", "false")

    return True if _CI == "true" else False
