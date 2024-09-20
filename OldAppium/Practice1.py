import time

from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
#from appium.options.android import UiAutomator2Options

#setting up driver by using desired capabilities
#options = UiAutomator2Options()
#options.load_capabilities(desired_caps)
#driver = webdriver.Remote("http://127.0.0.1:4723", options=options)


class FirstLaunch:

    def first(self):

        desired_caps = {

            "appium:platformName": "Android",
            "appium:deviceName": "95HX20SY9",
            "appium:automationName": "UiAutomator2",
            "appium:app": r"C:\\Users\\User\\Downloads\\buyer.apk",
            "appium:autoGrantPermissions": False,
            "appium:fullReset": False,
            "appium:noReset": True

        }

        driver = webdriver.Remote("http://127.0.0.1:4723",options=AppiumOptions().load_capabilities(desired_caps))

        time.sleep(5)
        driver.find_element(by=AppiumBy.XPATH, value=r'//android.widget.Button['
                                                     r'@resource-id="com.android.permissioncontroller:'
                                                     r'id/permission_allow_foreground_only_button"]').click()
        time.sleep(2)
        driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Skip').click()

        driver.quit()


class SecondLaunch:

    def second(self):

        desired_caps1 = {

            "appium:platformName": "Android",
            "appium:deviceName": "95HX20SY9",
            "appium:automationName": "UiAutomator2",
            "appium:autoGrantPermissions": True,
            "appium:appPackage": "com.lntsufin.buyer.sit2",
            "appium:appActivity": "com.lntsufin.buyer.MainActivity"
        }

        driver1 = webdriver.Remote("http://127.0.0.1:4723", options=AppiumOptions().load_capabilities(desired_caps1))

        driver1.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Skip').click()
        driver1.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@text="Next"]').click()
        driver1.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@text="Next"]').click()
        driver1.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@text="Close"]').click()

        driver1.find_element(by=AppiumBy.ID, value='searchid').click()
        driver1.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText').send_keys('anchor bolts')

        time.sleep(5)
        driver1.quit()


user = FirstLaunch()
user1 = SecondLaunch()
user.first()
user1.second()
