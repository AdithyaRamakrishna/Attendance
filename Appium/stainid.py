import time
from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import subprocess


class LaunchApp:

    def second(self):

        desired_caps = {

            "platformName": "Android",
            "appium:deviceName": "RZCW41Q2A0T",
            "appium:automationName": "UiAutomator2",
            "appium:app": "C:\\Users\\Adithya\\OneDrive\\Desktop\\stainid.apk",
            "appium:ensureWebviewsHavePages": True,
            "appium:nativeWebScreenshot": True,
            "appium:newCommandTimeout": 3600,
            "appium:connectHardwareKeyboard": True,
            "chromedriverExecutable": r"C:\Users\Adithya\Downloads\chromedriver.exe"

        }

        driver1 = webdriver.Remote("http://127.0.0.1:4723", options=AppiumOptions().load_capabilities(desired_caps))

        time.sleep(2)
        # contexts = driver1.contexts
        # print('Available contexts are : ', contexts)
        #
        # for i in range(2):
        #     contexts = driver1.contexts
        #     print('Available contexts are : ', contexts)
        #     if 'WEBVIEW' in contexts:
        #         driver1.switch_to.context('WEBVIEW')
        #         print('Switched to WEBVIEW context')
        #         break
        #     time.sleep(2)
        # else:
        #     print("WEBVIEW context not found")

        time.sleep(2)
        print('opened the app')
        time.sleep(2)

        wait = WebDriverWait(driver1, 20)
        element = wait.until(EC.presence_of_element_located(
            (AppiumBy.XPATH, "//android.view.View[@resource-id='ecolabs-connect-sign-in']")))
        element.click()
        print('clicked on email')

        element = wait.until(
            EC.element_to_be_clickable((AppiumBy.XPATH, "//android.widget.EditText[@resource-id='signInName']")))
        element.click()  # Ensure the element is focused
        element.send_keys('emcamanager@outlook.com')

        print('entered email')
        time.sleep(5)
        driver1.find_element(by=AppiumBy.XPATH,value='//android.widget.Button[@resource-id="continue"]').click()
        print('clicked on continue button')
        time.sleep(5)
        driver1.find_element(by=AppiumBy.XPATH,value='//android.widget.EditText[@resource-id="password"]').send_keys('!Ecolab1')
        print('entered password')
        time.sleep(2)
        driver1.find_element(by=AppiumBy.XPATH,value='//android.widget.Button[@resource-id="next"]').click()
        print('clicked on next button')
        time.sleep(5)
        driver1.find_element(by=AppiumBy.XPATH,value='//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_allow_foreground_only_button"]').click()
        print('allowed 1st permission')
        time.sleep(2)
        driver1.find_element(by=AppiumBy.XPATH,value='//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_allow_foreground_only_button"]').click()
        print('allowed 2nd permission')
        time.sleep(2)
        driver1.find_element(by=AppiumBy.XPATH,value='//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_allow_button"]').click()
        print('allowed 3rd permission')
        time.sleep(2)
        driver1.find_element(by=AppiumBy.XPATH,value='(//android.widget.TextView[@text="English"])[1]').click()
        print('selected english')
        time.sleep(2)
        driver1.find_element(by=AppiumBy.XPATH,value='//android.widget.Button[@text="Apply"]').click()
        print('clicked on apply button')
        time.sleep(2)
        driver1.find_element(by=AppiumBy.XPATH,value='//android.widget.Button[@text="Skip Pairing"]').click()
        print('skipped the bluetooth pairing')
        time.sleep(5)
        print('i am in the home screen')
        time.sleep(10)


'''
        x = 387
        y = 1203

        driver1.tap([(x, y)])

        driver1.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@text="Next"]').click()
        time.sleep(2)
        driver1.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@text="Next"]').click()
        time.sleep(2)
        driver1.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@text="Close"]').click()
        time.sleep(2)
        driver1.find_element(by=AppiumBy.ID, value='searchid').click()
        driver1.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText').send_keys('anchor bolts')
'''


user = LaunchApp()
user.second()


print('end')