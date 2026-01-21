from ui_tests.pages.login_page import LoginPage
from ui_tests.pages.inventory_page import InventoryPage


def test_login_positive(driver):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)

    login.open()
    login.login("standard_user", "secret_sauce")

    assert inventory.is_inventory_displayed()
