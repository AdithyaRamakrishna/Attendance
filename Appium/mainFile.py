# mainFile.py

import time
from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test import FreshLaunchApp  # Importing the login class from test.py


class AppLaunch:

    def __init__(self):
        self.driver = None
        self.wait = None

    def ex_setup(self):
        desired_caps = {
            "platformName": "Android",
            "appium:deviceName": "RZCW41Q2A0T",   # real device (Samsung S23)
            # "appium:deviceName": "emulator-5554 ",
            "appium:automationName": "UiAutomator2",
            "appium:appPackage": "com.ecolab.apps.stainid",
            "appium:appActivity": "crc64d83ff2e5b463b76a.MainActivity",
            # "appium:app": "C:\\Users\\Adithya\\OneDrive\\Desktop\\stainid.apk",
            "appium:noReset": True,  # Avoid reinstalling the app every time
            "appium:fullReset": False,
            "appium:ensureWebviewsHavePages": True,
            "appium:nativeWebScreenshot": True,
            "appium:newCommandTimeout": 3600,
            "appium:connectHardwareKeyboard": True
        }

        self.driver = webdriver.Remote("http://127.0.0.1:4723", options=AppiumOptions().load_capabilities(desired_caps))
        print('App opened from mainFile')
        self.wait = WebDriverWait(self.driver, 20)

        self.check_and_enable_internet()

    def check_and_enable_internet(self):
        # Get current network connection status
        connection_status = self.driver.network_connection

        # Network connection states in Android:
        # 0: Airplane Mode
        # 1: No Connection
        # 2: Wi-Fi Only
        # 4: Data Only
        # 6: All network (Wi-Fi + Data)

        if connection_status in [1, 0]:  # No Connection or Airplane mode
            print("Internet is OFF. Turning it ON...")
            # Enable both Wi-Fi and Data
            self.driver.set_network_connection(6)  # Enable Wi-Fi and Data
            print("Internet has been turned ON.")
        else:
            print("Internet is already ON. Skipping...")

        self.check_login()

    def check_login(self):
        try:
            # Check if already logged in by checking the presence of the home screen element
            self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Home']")))
            print("Already logged in. No need to log in again.")
            home_flow = FreshLaunchApp()
            home_flow.home()

        except Exception:
            print("Not logged in. Proceeding with login.")
            self.perform_login()

    def perform_login(self):
        # Calling the login flow from test.py
        login_flow = FreshLaunchApp()
        login_flow.login()


# Main execution
if __name__ == "__main__":
    user = AppLaunch()
    user.ex_setup()