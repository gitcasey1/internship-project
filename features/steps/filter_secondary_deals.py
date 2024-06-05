from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@given('Open the main page')
def open_main_page(context):
    context.app.main_page.open_main()


@when('Click Sign in')
def click_sign_in(context):
    context.app.main_page.click_sign_in()


@when('Input {email} into email field')
def input_email(context, email):
    context.app.sign_in_page.email_field(email)


@when('Input {password} into password field')
def input_password(context, password):
    context.app.sign_in_page.password_field(password)


@when('Log in to the page')
def log_in(context):
    context.app.sign_in_page.click_continue_button()


@when('Click on Secondary option at the left side menu')
def click_secondary_option(context):
    context.app.left_side_menu.click_secondary_option()


@then('Verify the right page opens')
def verify_right_page_opens(context):
    context.app.secondary_page.verify_all_listings()


@when('Click Filters button at top center of page')
def click_filters_button(context):
    sleep(5)
    # context.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Filters']")))
    context.app.secondary_page.click_filters_button()


@when('Input Unit price (AED) from {from_price}')
def input_unit_from(context, from_price):
    sleep(5)
    # context.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[wized='unitPriceFromFilter']")))
    context.app.secondary_page.from_field(from_price)


@when('Input Unit price (AED) to {to_price}')
def input_unit_to(context, to_price):
    sleep(5)
    # context.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[wized='unitPriceToFilter']")))
    context.app.secondary_page.to_field(to_price)


@when('Click Apply filter button')
def click_apply_filter(context):
    sleep(10)
    # context.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[wized='applyFilterButtonMLS']")))
    context.app.secondary_page.click_apply_filter_button()
    sleep(2)


@then('Verify the price in all cards is inside the range ({from_price} - {to_price})')
def verify_price_in_range(context, from_price, to_price):
    context.app.secondary_page.range_in_prices(from_price, to_price)
