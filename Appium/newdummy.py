from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test import FreshLaunchApp
import time

desired_caps = {
    "platformName": "Android",
    "appium:deviceName": "RZCW41Q2A0T",  # real device (Samsung S23)
    "appium:automationName": "UiAutomator2",
    "appium:app": r"C:\Users\Adithya\Downloads\6.0.184077.apk",
}

driver = webdriver.Remote("http://127.0.0.1:4723", options=AppiumOptions().load_capabilities(desired_caps))
time.sleep(10)

wait = WebDriverWait(driver, 10)

elo = driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@resource-id="ecolabs-connect-sign-in"]')
wait.until(EC.element_to_be_clickable(elo))
elo.click()
el1 = driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.EditText")
el1.click()
el1.send_keys("emcamanager@outlook.com")
el2 = driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.Button")
el2.click()
el3 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().resourceId(\"password\")")
el3.click()
el3.send_keys("!Ecolab1")
el4 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().resourceId(\"next\")")
el4.click()
el5 = driver.find_element(by=AppiumBy.ID, value="com.android.permissioncontroller:id/permission_allow_foreground_only_button")
el5.click()
el6 = driver.find_element(by=AppiumBy.ID, value="com.android.permissioncontroller:id/permission_allow_foreground_only_button")
el6.click()
el7 = driver.find_element(by=AppiumBy.ID, value="com.android.permissioncontroller:id/permission_allow_button")
el7.click()
el8 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Apply\")")
el8.click()
el9 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Continue\")")
el9.click()
el10 = driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.CheckBox")
el10.click()
el11 = driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.Button")
el11.click()


driver.find_element(AppiumBy.XPATH)