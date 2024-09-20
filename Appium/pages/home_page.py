from Appium.config.import_items import *
from Appium.config.import_items import WaitActions


class HomePage:

    def adding_waits(self):

        actions = WaitActions(self)
        actions.wait_and_click(self)
        actions.wait_and_send_keys(self)

    def __init__(self, driver=None):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 40)

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