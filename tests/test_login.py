import pytest
from playwright.sync_api import Playwright
from common.base import BasePage
from config.browser_manager import BrowserManager
from config.config_manager import Config_Manager
from pages.login import LoginPage


@pytest.mark.usefixtures
def test(playwright: Playwright):
    page = BrowserManager.launch_browser(playwright)
    BasePage(page).url(Config_Manager.url())
    BasePage(page).sleep(2000)
    LoginPage(page).enter_username("Test")
    LoginPage(page).click_login_button()
    BasePage(page).sleep(2000)
    BasePage(page).close()
