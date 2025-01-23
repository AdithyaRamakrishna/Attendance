# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# driver = webdriver.Chrome()
#
# driver.get('https://www.cricbuzz.com/')
# print(driver.title)
# print(driver.current_url)
# print(driver.current_window_handle)
# print(driver.window_handles)
# #print(driver.page_source)
# driver.find_element(By.ID,'newsDropDown').click()
# driver.find_element(By.CLASS_NAME, 'cb-hm-mnu-itm').click()
# time.sleep(1)
# driver.back()
# time.sleep(2)
#
# driver.forward()
# time.sleep(2)
# driver.refresh()
# #driver.switch_to.new_window('tab')
# driver.maximize_window()
# time.sleep(2)
# #driver.set_window_size(400,400)
# driver.fullscreen_window()
# time.sleep(2)
# #driver.delete_all_cookies()
# #driver.close()
# time.sleep(2)
# #driver.quit()
#
# driver.find_element(By.CSS_SELECTOR("#newsDropDown"))
# time.sleep(2)
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

# driver.get("https://rahulshettyacademy.com/angularpractice/")
# driver.maximize_window()
#
# driver.find_element(By.XPATH, "//label[text() = 'Name']//following-sibling::input").send_keys('Adithya')
# driver.find_element(By.CSS_SELECTOR, "input[name = 'email']").send_keys('hello@gmail.com')
# driver.find_element(By.ID, "exampleInputPassword1").send_keys('123456')
# driver.find_element(By.ID, "exampleCheck1").click()
# driver.find_element(By.CSS_SELECTOR, "#inlineRadio2").click()
# driver.find_element(By.XPATH, "//input[@type = 'submit']").click()

# # static dropdown
# gender_dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
# gender_dropdown.select_by_index(1)
# gender_dropdown.select_by_visible_text('Female')

# dynamic dropdown

# driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
# driver.maximize_window()
# driver.find_element(By.ID, "autosuggest").send_keys('In')
# time.sleep(2)
# countries = driver.find_elements(By.XPATH, "//li[@class = 'ui-menu-item']/a")
# print(len(countries))
#
# for country in countries:
#     if country.text == 'India':
#         country.click()
#         break
# assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == 'India'
#
# # radio button
#
# radiobutton = driver.find_elements(By.XPATH, "//table[@id = 'ctl00_mainContent_rbtnl_Trip']//td")
# radiobutton[2].click()
# time.sleep(2)
#
# time.sleep(2)
# for radio in radiobutton:
#     if radio.text == 'Multicity':
#         radio.click()
#         time.sleep(3)

# # search and click the suggestion
# driver.get("https://www.flipkart.com/")
# driver.find_element(By.XPATH, "//input[@class = 'Pke_EE' and @name = 'q']").send_keys('mobile')
# time.sleep(3)
# suggestions = driver.find_elements(By.XPATH, "//li[@class = '_3D0G9a']/div")
#
# print(len(suggestions))
#
# for suggestion in suggestions:
#     if suggestion.text == 'mobile cover':
#         suggestion.click()
#         break

# # checkbox action for dynamic elements
# driver.get("https://www.flipkart.com/mobiles/mi~brand/pr?sid=tyy,4io&otracker=nmenu_sub_Electronics_0_Mi")
# time.sleep(2)
# checkboxes = driver.find_elements(By.XPATH, "//div[@class = 'ewzVkT _3DvUAf']")
# for check in checkboxes:
#     if check.get_attribute("title") == "3 GB":
#         check.click()
#         break

# handling alerts
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.ID, "name").send_keys('adithya')
driver.find_element(By.ID, "alertbtn").click()
time.sleep(2)
alert = driver.switch_to.alert
alerttext = alert.text
print(alerttext)
alert.accept()
time.sleep(1)

assert 'adithya' in alerttext
