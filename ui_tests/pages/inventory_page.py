from selenium.webdriver.common.by import By
from ui_tests.pages.base_page import BasePage


class InventoryPage(BasePage):
    INVENTORY_LIST = (By.CLASS_NAME, "inventory_list")

    def is_inventory_displayed(self):
        return self.wait_for_visibility(self.INVENTORY_LIST).is_displayed()
