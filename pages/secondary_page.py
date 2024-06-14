from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage


class SecondaryPage(BasePage):
    SECONDARY_ALL_LISTINGS = (By.XPATH, "//a[text()='All listings']")
    FILTERS_BUTTON = (By.XPATH, "//div[text()='Filters']")
    AED_FROM_FIELD = (By.CSS_SELECTOR, "input[wized='unitPriceFromFilter']")
    AED_TO_FIELD = (By.CSS_SELECTOR, "input[wized='unitPriceToFilter']")
    APPLY_FILTER_BUTTON = (By.CSS_SELECTOR, "a[wized='applyFilterButtonMLS']")
    PRICES = (By.XPATH, "//div[@class='price-aed-block']")
    MOBILE_WEB_LISTINGS_AGENTS = (By.CSS_SELECTOR, "div.proparties_text_block.secondary")

    def verify_all_listings(self):
        self.wait_until_visible(*self.SECONDARY_ALL_LISTINGS)

    def click_filters_button(self):
        self.click(*self.FILTERS_BUTTON)
        # self.wait_until_clickable_click(*self.FILTERS_BUTTON)

    def from_field(self, amount):
        self.input_text(amount,*self.AED_FROM_FIELD)
        # self.wait_until_visible(*self.AED_FROM_FIELD)

    def to_field(self, amount):
        self.input_text(amount,*self.AED_TO_FIELD)
        # self.wait_until_visible(*self.AED_TO_FIELD)

    def click_apply_filter_button(self):
        # self.click(*self.APPLY_FILTER_BUTTON)
        self.wait_until_clickable_click(*self.APPLY_FILTER_BUTTON)

    def range_in_prices(self, from_price, to_price):
        all_prices = self.driver.find_elements(*self.PRICES)
        from_price = int(from_price)
        to_price = int(to_price)

        for price in all_prices:
            price = int(price.text.replace("AED", "").replace(",", "").strip())
            assert from_price <= price <= to_price, f"Price {price} is not in the expected range."

    def verify_mobile_listings_agents(self):
        self.wait_until_visible(*self.MOBILE_WEB_LISTINGS_AGENTS)
