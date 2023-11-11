from playwright.sync_api import Page


class BasePage:

    def __init__(self, page: Page):
        self.page = page

    def url(self, URL):
        self.page.goto(URL)

        return self

    def close(self):
        self.page.close()

    def sleep(self, time):
        self.page.wait_for_timeout(int(time))
        return self
