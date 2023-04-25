from appium.webdriver.common.appiumby import AppiumBy as By
from screens.base_Screen import BaseScreen


class HomeScreen(BaseScreen):

    def __init__(self, driver):
        self.txt_user = (By.ACCESSIBILITY_ID, "test-Username")
        self.txt_pass = (By.ACCESSIBILITY_ID, "test-Password")
        self.btn_login = (By.ACCESSIBILITY_ID, "test-LOGIN")
        super().__init__(driver)

    def login(self, username, password):
        self.driver.find_element(*self.txt_user).send_keys(username)
        self.driver.find_element(*self.txt_pass).send_keys(password)
        self.driver.find_element(*self.btn_login).click()



