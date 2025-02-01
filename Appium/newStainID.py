
# newStainID.py


import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.common import AppiumOptions
from selenium.common import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class FreshLaunchApp:

    def __init__(self):
        self.driver = None
        self.wait = None

    def des_capabilities(self):

        desired_caps = {

            "platformName": "Android",
            "appium:deviceName": "Android device",
            "appium:automationName": "UiAutomator2",
            # "appium:app": r"C:\Users\Adithya\OneDrive\Desktop\7.2.256994_QA.apk",
            "appium:appPackage": "com.ecolab.apps.stainid",
            "appium:appActivity": "com.ecolab.apps.stainid.MainActivity",
            "appium:ensureWebviewsHavePages": True,
            "appium:nativeWebScreenshot": True,
            "appium:newCommandTimeout": 3600,
            "appium:connectHardwareKeyboard": True,
            "appium:noReset": True,
            "appium:fullReset": False,

        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723", options=AppiumOptions().load_capabilities(desired_caps))
        self.wait = WebDriverWait(self.driver, 20)  # Initialize WebDriverWait after driver is created

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

    def wait_and_get_text(self, locator, description):
        print(f'Waiting for {description}')
        element = self.wait.until(EC.presence_of_element_located(locator))
        text = element.text
        print(f'{description}: {text} message is shown on the screen')
        return text  # Return the text so it can be used elsewhere

    def wait_until_enabled_and_click(self, locator, description):
        print(f'Waiting for {description} to appear...')
        element = self.wait.until(EC.presence_of_element_located(locator))
        print(f'Checking if {description} is enabled...')
        self.wait.until(lambda d: d.find_element(*locator).is_enabled())
        print(f'{description} is now enabled. Clicking it...')
        element.click()

    def wait_and_scroll(self, start_x, start_y, end_x, end_y, times=1, description="scroll action"):
        print(f"Waiting for {description}")

        # Perform the scroll action `times` times
        for _ in range(times):
            actions = ActionChains(self.driver)
            actions.w3c_actions.pointer_action.move_to_location(start_x, start_y)  # Starting point of swipe
            actions.w3c_actions.pointer_action.pointer_down()  # Press down to start swipe
            actions.w3c_actions.pointer_action.move_to_location(end_x, end_y)  # End point of swipe
            actions.w3c_actions.pointer_action.release()  # Release the swipe
            actions.perform()  # Perform the swipe action
            time.sleep(1)  # Optional: wait for a second between swipes

        print(f"Performed {times} {description}")

    def check_login(self):
        try:
            # Check if already logged in by checking the presence and visibility of the home screen element
            self.wait.until(
                EC.visibility_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Home']")))
            print("Already logged in. No need to log in again.")
            self.navigate_to_home_screen()

        except Exception:
            print("Not logged in. Proceeding with login.")
            self.login()

    def login(self):

        time.sleep(5)
        # Click on email sign-in
        # self.wait_and_click((AppiumBy.ID, '//android.widget.EditText[@resource-id="i0116"]'), "Email Sign-In")

        # Enter email
        self.wait_and_send_keys((AppiumBy.XPATH, '//android.widget.EditText[@resource-id="i0116"]'), 'adithya.r@ecolab.com', "Email Field")

        # Old implementatiom
        # Click anywhere on the screen
        # self.wait_and_click((AppiumBy.XPATH, '//android.widget.Image[@text="login_header"]'), 'Clicked on Ecolab logo')

        # Old implementation
        # Click on the continue button
        # self.wait_and_click((AppiumBy.XPATH, "//android.widget.Button[@resource-id='continue']"), "Continue Button")

        # Click on the next button
        self.wait_and_click((AppiumBy.XPATH, '//android.widget.Button[@resource-id="idSIButton9"]'), "Next Button")

        # Old implementation
        # Enter password
        # self.wait_and_send_keys((AppiumBy.XPATH, "//android.widget.EditText[@resource-id='password']"), '!Ecolab1', "Password Field")

        # Old Implementation
        # Click on the next button
        # self.wait_and_click((AppiumBy.XPATH, "//android.widget.Button[@resource-id='next']"), "Next Button")

        self.app_permission()

    def app_permission(self):

        # Handle permissions
        self.wait_and_click((AppiumBy.XPATH, "//android.widget.Button[@resource-id='com.android.permissioncontroller:id/permission_allow_foreground_only_button']"), "First Permission")
        self.wait_and_click((AppiumBy.XPATH, "//android.widget.Button[@resource-id='com.android.permissioncontroller:id/permission_allow_foreground_only_button']"), "Second Permission")
        self.wait_and_click((AppiumBy.XPATH, "//android.widget.Button[@resource-id='com.android.permissioncontroller:id/permission_allow_button']"), "Third Permission")

        self.language_selection()

    def language_selection(self):

        # Select English language
        self.wait_and_click((AppiumBy.XPATH, "(//android.widget.TextView[@text='English'])[1]"), "English Language")

        # Apply language settings
        self.wait_and_click((AppiumBy.XPATH, "//android.widget.Button[@text='Apply']"), "Apply Button")

        # Continue Bluetooth pairing
        # self.wait_and_click((AppiumBy.XPATH, '//android.widget.Button[@text="Continue"]'), "Continue Pairing")

        # Skip Bluetooth pairing
        self.wait_and_click((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Skip Pairing")'), "Skip Pairing")


        # navigate to home screen
        self.navigate_to_home_screen()

    def navigate_to_home_screen(self):
        print('Navigated to the Home Screen')
        # Now perform actions on the home screen

        #self.wait_until_enabled_and_click((AppiumBy.XPATH, 'new UiSelector().className("android.widget.ImageView").instance(3)'), "New Scan Button")

        self.wait_and_click((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(10)'),"New Scan")

        self.home_actions()

    def home_actions(self):
        print('Performing home actions...')
        self.home_search()

    def hamburger(self):
        pass

    def scan_new_sample(self):

        # Click on + button
        self.wait_and_click((AppiumBy.XPATH, '//android.widget.Button[@text="+"]'), "+ button")

    def account_number(self):

        # Open the Account Detail screen
        self.wait_and_click((AppiumBy.XPATH,'//androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView[3]'),'Account Detail screen')
        print("Opened the Account Detail screen")

        # Scroll Previous Scans
        self.wait_and_scroll(start_x=500, start_y=2000, end_x=500, end_y=1640, times=3, description="Account Detail scrolling")
        print('Performed the scrolling action')

        # Navigate back to Home screen
        self.wait_and_click((AppiumBy.XPATH,'//androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ImageView'),'Back Arrow')
        print('Clicked on the back arrow')

        print('Navigated to Home screen')

    def scan_card(self):

        # Open the Scan Card
        self.wait_and_click(
            (AppiumBy.XPATH, '//androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup'),'Scan Card')
        print("Opened the first scan card")

        # Scan Feedback
        value = 1      # [0 = Yes, 1 = Not sure, 2 = No]
        if value == 0:
            self.wait_and_click((AppiumBy.XPATH, '//android.widget.TextView[@text="Yes"]'),'Yes')
            text = self.wait_and_get_text((AppiumBy.XPATH,'//android.widget.TextView[@text="Thank You!"]'),'Thank You')
            assert 'Thank You' in text, 'You have not opted YES'

        elif value == 1:
            self.wait_and_click((AppiumBy.XPATH, '//android.widget.TextView[@text="Not sure"]'),'Not sure')
            text = self.wait_and_get_text((AppiumBy.XPATH,'//android.widget.TextView[@text="Thank You!"]'),'Thank You')
            assert 'Thank You' in text

        else:
            self.wait_and_click((AppiumBy.XPATH, '//android.widget.TextView[@text="No"]'),'No')
            text = self.wait_and_get_text((AppiumBy.XPATH,'//android.widget.TextView[@text="Sorry!"]'),'Sorry')
            assert 'Sorry' in text

            # Entering the Feedback
            self.wait_and_send_keys((AppiumBy.CLASS_NAME,'android.widget.EditText'),'This is wrong identification','Feedback box')

            # Click on Submit Button
            self.wait_and_click((AppiumBy.XPATH,'//android.widget.Button[@text="Submit"]'),'Submit')
            # assert 'Thank You' in text

            # Click on Skip Button
            # self.wait_and_click((AppiumBy.XPATH,'//android.widget.Button[@text="Skip"]'),'Skip Button')

        # Click on X icon
        time.sleep(5)
        self.wait_and_click((AppiumBy.XPATH, '//androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ImageView'), 'X icon')

        print('Navigated back to home screen')

        self.account_number()

    def home_search(self):

        print('performing searching')
        # Locate the search bar element
        search_bar = "com.ecolab.apps.stainid:id/search_src_text"

        # Click on search bar
        self.wait_and_click((AppiumBy.ID, search_bar), "Search Bar")

        # Enter search key [Stain Name]
        self.wait_and_send_keys((AppiumBy.ID, search_bar), 'Mascara', "Enter Search Key")

        # Close the keyboard
        # self.driver.hide_keyboard()
        self.driver.press_keycode(4)  # Keycode for the Back button

        # Perform scrolling action
        self.wait_and_scroll(start_x=500, start_y=1800, end_x=500, end_y=500, times=1, description="scroll on the home screen")

        print('Scrolled down')

        # Clear the searched item
        self.wait_and_click((AppiumBy.ID, 'com.ecolab.apps.stainid:id/search_close_btn'),'Clear Search button')
        print('Cleared the search text')

        # Enter search key [Account Name]
        self.wait_and_send_keys((AppiumBy.ID, search_bar), 'Ecolab', "Enter Search Key")

        # Close the keyboard
        self.driver.press_keycode(4)  # Keycode for the Back button
        time.sleep(2)

        # Perform scrolling action
        self.wait_and_scroll(start_x=500, start_y=1800, end_x=500, end_y=500, times=1, description="scroll on the home screen")
        print('Scrolled down')
        time.sleep(2)

        self.scan_card()


app = FreshLaunchApp()
app.des_capabilities()
app.check_login()
