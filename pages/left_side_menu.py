from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LeftSideMenu(BasePage):
    SECONDARY_OPTION = (By.XPATH, "//div[text()='Secondary']")

    def click_secondary_option(self):
        self.click(*self.SECONDARY_OPTION)