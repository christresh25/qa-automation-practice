from ui_tests.pages.inventory_page import InventoryPage
from ui_tests.pages.login_page import LoginPage

def test_sort_products(setup):
    LoginPage(setup).login("standard_user", "secret_sauce")
    inventory = InventoryPage(setup)
    inventory.sort_products ("lohi")
    inventory.add_product_to_cart()
    assert inventory.cart_count() ==1