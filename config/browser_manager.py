from playwright.sync_api import Playwright, Browser, BrowserType
from config.config_manager import Config_Manager


class BrowserManager:

    @staticmethod
    def launch_browser(self: Playwright) -> Browser:
        return BrowserManager.browser(self).launch(channel=Config_Manager.channel(), headless=Config_Manager.headless(),
                                                   args=["--start-maximized"]).new_context(
            no_viewport=True).new_page()

    @staticmethod
    def browser(self: Playwright) -> BrowserType:

        driver = Config_Manager.browser()
            
        if driver == "chromium":
            return self.chromium

        elif driver == "firefox":
            return self.firefox

        else:
            return self.webkit
