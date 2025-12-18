from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)   # 👈 Explicit wait

    sort_dropdown = (By.CLASS_NAME, "product_sort_container")
    add_to_cart = (By.ID, "add-to-cart-sauce-labs-backpack")
    cart_badge = (By.CLASS_NAME, "shopping_cart_badge")

    def sort_products(self, value):
        dropdown = self.wait.until(
            EC.visibility_of_element_located(self.sort_dropdown)
        )
        Select(dropdown).select_by_value(value)

    def add_product_to_cart(self):
        self.wait.until(
            EC.element_to_be_clickable(self.add_to_cart)
        ).click()

    def cart_count(self):
        return int(self.wait.until(
            EC.visibility_of_element_located(self.cart_badge)
        ).text)
