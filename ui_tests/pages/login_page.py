from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
    username=(By.ID, "user-name")
    password=(By.ID, "password")
    login_btn=(By.ID, "login-button")
    error_msg = (By.XPATH, "//h3[@data-test='error']")

    def login(self, user, pwd):
        self.wait.until(EC.visibility_of_element_located(self.username)).send_keys(user)
        self.wait.until(EC.visibility_of_element_located(self.password)).send_keys(pwd)
        self.wait.until(EC.element_to_be_clickable(self.login_btn)).click()

    def get_error(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.error_msg)).text