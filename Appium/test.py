import time
from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FreshLaunchApp:

    def __init__(self, driver=None):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 40)

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

    def login(self):
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

        # Handle permissions
        self.wait_and_click((AppiumBy.XPATH, "//android.widget.Button[@resource-id='com.android.permissioncontroller:id/permission_allow_foreground_only_button']"), "First Permission")
        self.wait_and_click((AppiumBy.XPATH, "//android.widget.Button[@resource-id='com.android.permissioncontroller:id/permission_allow_foreground_only_button']"), "Second Permission")
        self.wait_and_click((AppiumBy.XPATH, "//android.widget.Button[@resource-id='com.android.permissioncontroller:id/permission_allow_button']"), "Third Permission")

        # Select English language
        self.wait_and_click((AppiumBy.XPATH, "(//android.widget.TextView[@text='English'])[1]"), "English Language")

        # Apply language settings
        self.wait_and_click((AppiumBy.XPATH, "//android.widget.Button[@text='Apply']"), "Apply Button")

        # Skip Bluetooth pairing
        self.wait_and_click((AppiumBy.XPATH, "//android.widget.Button[@text='Skip Pairing']"), "Skip Pairing")

        self.home()


    def home(self):
        print('On the Home Screen')
        time.sleep(5)
        # Wait until the '+' button becomes clickable
        button_xpath = '//android.widget.Button[@text="+"]'
        print(f'Waiting for the + button to be clickable')
        try:
            self.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, button_xpath)))
            print('Button is clickable now. Proceeding with actions.')
            # Interact with the button
            self.driver.find_element(by=AppiumBy.XPATH, value=button_xpath).click()
            print('Clicked on the "+" button.')
        except Exception as e:
            print(f'An error occurred while waiting for the button to be clickable: {e}')

