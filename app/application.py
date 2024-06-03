from pages.base_page import BasePage
from pages.left_side_menu import LeftSideMenu
from pages.main_page import MainPage
from pages.secondary_page import SecondaryPage
from pages.sign_in_page import SignInPage


class Application:

    def __init__(self, driver):
        self.base_page = BasePage(driver)
        self.left_side_menu = LeftSideMenu(driver)
        self.main_page = MainPage(driver)
        self.secondary_page = SecondaryPage(driver)
        self.sign_in_page = SignInPage(driver)
