import time
from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test import FreshLaunchApp  # Importing the login class from test.py# from Appium.utils.wait_utilis import WaitUtils



class LoginPage:
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

    def login(self, email, password):
        # Click on email sign-in
        self.wait_and_click((AppiumBy.XPATH, "//android.view.View[@resource-id='ecolabs-connect-sign-in']"), "Email Sign-In")

        # Enter email
        self.wait_and_send_keys((AppiumBy.XPATH, "//android.widget.EditText[@resource-id='signInName']"), 'emcamanager@outlook.com', "Email Field")

        # Click anywhere on the screen
        self.wait_and_click((AppiumBy.XPATH, '//android.widget.Image[@text="login_header"]'), 'Clicked on Ecolab logo')

        # Click on the continue button
        self.wait_and_click((AppiumBy.XPATH, "//android.widget.Button[@resource-id='continue']"), "Continue Button")

        # Enter password
        self.wait_and_send_keys((AppiumBy.XPATH, "//android.widget.EditText[@resource-id='password']"), '!Ecolab1', "Password Field")

        # Click on the next button
        self.wait_and_click((AppiumBy.XPATH, "//android.widget.Button[@resource-id='next']"), "Next Button")