from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SignInPage(BasePage):
    EMAIL_FIELD = (By.ID, 'email-2')
    PASSWORD_FIELD = (By.ID, 'field')
    CONTINUE_BUTTON = (By.XPATH, "//a[@wized='loginButton']")

    def email_field(self, email):
        self.input_text(email, *self.EMAIL_FIELD)

    def password_field(self, password):
        self.input_text(password, *self.PASSWORD_FIELD)

    def click_continue_button(self) -> object:
        self.click(*self.CONTINUE_BUTTON)
