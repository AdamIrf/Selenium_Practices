from selenium import webdriver

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_checkout_flow():

    driver = webdriver.Chrome()

    driver.get("https://www.saucedemo.com")

    # Login
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")

    # Inventory
    inventory = InventoryPage(driver)
    inventory.add_backpack()
    inventory.open_cart()

    # Cart
    cart = CartPage(driver)
    cart.checkout()

    # Checkout
    checkout = CheckoutPage(driver)

    checkout.fill_info(
        "Adam",
        "Irfan",
        "32610"
    )

    checkout.finish_order()

    assert checkout.get_success_message() == \
           "Thank you for your order!"

    driver.quit()