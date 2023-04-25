import pytest
from screens.HomeScreen import HomeScreen
from screens.ProductScreen import ProductScreen

user = "standard_user"
passwd = "secret_sauce"


@pytest.mark.regression
def test_successful_login(driver):
    home_screen = HomeScreen(driver)
    home_screen.login(user, passwd)
    #assert ProductScreen.title()

user1 = "admin"
passwd1 = "Corrito123"

@pytest.mark.regression
def test_error_login(driver):
    home_screen = HomeScreen(driver)
    home_screen.login(user1, passwd1)
    #assert ProductScreen.title()