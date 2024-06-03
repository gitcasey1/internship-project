from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):
    SIGN_IN = (By.XPATH, "//div[text()='Sign in']")

    def open_main(self):
        self.driver.get('https://soft.reelly.io/sign-up')

    def click_sign_in(self):
        self.click(*self.SIGN_IN)
