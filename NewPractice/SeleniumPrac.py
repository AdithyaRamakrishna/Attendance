from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get('https://www.cricbuzz.com/')
print(driver.title)
print(driver.current_url)
print(driver.current_window_handle)
print(driver.window_handles)
#print(driver.page_source)
driver.find_element(By.ID,'newsDropDown').click()
driver.find_element(By.CLASS_NAME, 'cb-hm-mnu-itm').click()
time.sleep(1)
driver.back()
time.sleep(2)

driver.forward()
time.sleep(2)
driver.refresh()
#driver.switch_to.new_window('tab')
driver.maximize_window()
time.sleep(2)
#driver.set_window_size(400,400)
driver.fullscreen_window()
time.sleep(2)
#driver.delete_all_cookies()
#driver.close()
time.sleep(2)
#driver.quit()

driver.find_element(By.CSS_SELECTOR("#newsDropDown"))
time.sleep(2)
