import time

from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy


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

        time.sleep(3)
        driver1.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Skip').click()
        time.sleep(5)

        x = 100
        y = 200

        driver1.tap([(x, y)])

        driver1.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@text="Next"]').click()
        time.sleep(2)
        driver1.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@text="Next"]').click()
        time.sleep(2)
        driver1.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@text="Close"]').click()
        time.sleep(2)
        driver1.find_element(by=AppiumBy.ID, value='searchid').click()
        driver1.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText').send_keys('anchor bolts')

        time.sleep(5)
        driver1.quit()


user1 = SecondLaunch()
user1.second()