from ui_tests.pages.login_page import LoginPage

def test_login_postive(setup):
    login = LoginPage(setup)
    login.login("standard_user", "secret_sauce")
    assert "inventory" in setup.current_url
def test_login_negative(setup):
    login = LoginPage(setup)
    login.login("standard_user", "secret_sau")
    assert "Username and password do not match" in login.get_error()