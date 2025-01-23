from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test import FreshLaunchApp  # Importing the login class from test.py# from Appium.utils.wait_utilis import WaitUtils


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def wait_and_click(self, locator, description):
        print(f'Waiting for {description}')
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
        print(f'Clicked on {description}')

    def wait_and_send_keys(self, locator, keys, description):
        print(f'Waiting for {description}')
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.clear()
        element.send_keys(keys)
        print(f'Entered {keys} into {description}')

    def permission(self):

        # Handle permissions
        self.wait_and_click((AppiumBy.XPATH,
                             "//android.widget.Button[@resource-id='com.android.permissioncontroller:id/"
                             "permission_allow_foreground_only_button']"), "First Permission")
        self.wait_and_click((AppiumBy.XPATH,
                             "//android.widget.Button[@resource-id='com.android.permissioncontroller:id/"
                             "permission_allow_foreground_only_button']"), "Second Permission")
        self.wait_and_click((AppiumBy.XPATH,
                             "//android.widget.Button[@resource-id='com.android.permissioncontroller:id/"
                             "permission_allow_button']"), "Third Permission")

        # Select English language
        self.wait_and_click((AppiumBy.XPATH, "(//android.widget.TextView[@text='English'])[1]"), "English Language")

        # Apply language settings
        self.wait_and_click((AppiumBy.XPATH, "//android.widget.Button[@text='Apply']"), "Apply Button")

        # Skip Bluetooth pairing
        self.wait_and_click((AppiumBy.XPATH, "//android.widget.Button[@text='Skip Pairing']"), "Skip Pairing")