import pytest
from appium import webdriver

DESIRED_CAPABILITIES = {
  "platformName": "Android",
  "deviceName": "N9AIOC167461KTH",
  "appName": "Swag Labs Mobile App",
  "appActivity": "com.swaglabsmobileapp.MainActivity",
  "app": "E:/Users/1068555/Escritorio/sauceLabs v1.0.apk"
}

URL = "http://127.0.0.1:4723/wd/hub"

# Fixture. Define el driver.
@pytest.fixture
def driver():
    wait_seconds = 5
    driver = webdriver.Remote(URL, DESIRED_CAPABILITIES)
    driver.implicitly_wait(wait_seconds)
    yield driver
    driver.quit()
