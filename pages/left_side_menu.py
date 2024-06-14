from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LeftSideMenu(BasePage):
    SECONDARY_OPTION = (By.XPATH, "//div[text()='Secondary']")
    MOBILE_WEB_SECONDARY_OPTION = (By.CSS_SELECTOR, "a[wized='mobileTabGame']")

    def click_secondary_option(self):
        self.click(*self.SECONDARY_OPTION)

    def click_mobile_secondary_option(self):
        self.click(*self.MOBILE_WEB_SECONDARY_OPTION)
