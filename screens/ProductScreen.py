from appium.webdriver.common.appiumby import AppiumBy as By
from screens.base_Screen import BaseScreen


class ProductScreen(BaseScreen):

    def __init__(self, driver):
        super().__init__(driver)
        self.title = (By.ANDROID_UIAUTOMATOR, 'text("PRODUCTS")')



