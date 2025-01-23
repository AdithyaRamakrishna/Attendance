
# test.py


import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class FreshLaunchApp:

    def __init__(self, driver=None):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

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

        time.sleep(5)
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

        # navigate to home screen
        self.navigate_to_home_screen()

    def navigate_to_home_screen(self):
        print('Navigated to the Home Screen')
        # Now perform actions on the home screen
        self.home_actions()

    def home_actions(self):
        print('Performing home actions...')
        self.home_search()

    def settings(self):
        pass

    def scan_new_sample(self):

        # Click on + button
        self.wait_and_click((AppiumBy.XPATH, '//android.widget.Button[@text="+"]'), "+ button")

    def account_number(self):
        pass

    def scan_card(self):

        # Open the Stain Card
        self.wait_and_click(
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(13)'),
            'Stain Card')

        # Click on X icon
        self.wait_and_click((AppiumBy.XPATH, '//android.widget.ScrollView/android.view.ViewGroup/android.'
                                             'view.ViewGroup/android.view.ViewGroup[1]/android.widget.ImageView'),
                            'X icon')

        print('navigated back to home screen')

    def home_search(self):

        print('performing searching')
        # Locate the search bar element
        search_bar = "com.ecolab.apps.stainid:id/search_src_text"

        # Click on search bar
        self.wait_and_click((AppiumBy.ID, search_bar), "Search Bar")

        # Enter search key
        self.wait_and_send_keys((AppiumBy.ID, search_bar), 'Mascara', "Enter Search Key")

        # Close the keyboard
        # self.driver.hide_keyboard()
        self.driver.press_keycode(4)  # Keycode for the Back button

        # Perform scroll using ActionChains
        actions = ActionChains(self.driver)
        actions.w3c_actions.pointer_action.move_to_location(500, 1800)  # Adjust based on your screen size
        actions.w3c_actions.pointer_action.pointer_down()               # Press down to start the scroll
        actions.w3c_actions.pointer_action.move_to_location(500, 500)  # Adjust based on your screen size
        actions.w3c_actions.pointer_action.release()                    # Release the pointer to complete the scroll
        actions.perform()                                               # Execute the scroll actions

        print('Scrolled down')

        self.driver.quit()

