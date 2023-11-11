from common.base import BasePage


class LoginPage(BasePage):

    def __init__(self, page):

        """
        :param page: handle locator using page object model (POM)
        """
        self.user_name_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.login_button = page.get_by_role("button", name="Login")

        """
        access parent class property into child class
        """
        BasePage.__init__(self, page)

    def enter_username(self, text: str):
        return self.user_name_input.fill(text.strip())

    def enter_password(self, text: str):
        return self.password_input().fill(text.strip())

    def click_login_button(self):
        return self.login_button.click()
