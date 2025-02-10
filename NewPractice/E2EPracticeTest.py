from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

driver.get('https://rahulshettyacademy.com/angularpractice/')
driver.maximize_window()

driver.find_element(By.XPATH,"//a[contains(@href , 'shop')]").click()
# driver.find_element(By.CSS_SELECTOR, "a[href* = 'shop]").click()

elements = driver.find_elements(By.XPATH, '//div[@class="card h-100"]')

for element in elements:
    productName = element.find_element(By.XPATH, 'div/h4/a').text
    if productName == 'Blackberry':
        element.find_element(By.XPATH , 'div/button').click()
        break
driver.find_element(By.XPATH, '//a[@class="nav-link btn btn-primary"]').click()

time.sleep(2)

driver.find_element(By.CSS_SELECTOR, 'button[class*="success"]').click()

# driver.find_element(By.ID, 'country').send_keys('land')
# time.sleep(5)
#
# countrySuggestions = driver.find_elements(By.XPATH, '//div[@class="suggestions"]/ul')
#
# for country in countrySuggestions:
#     if country == 'Poland':
#         country.click()
#         break

driver.find_element(By.ID, 'country').send_keys('land')
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,'Poland')))

driver.find_element(By.LINK_TEXT,'Poland').click()

driver.find_element(By.XPATH,"//label[@for='checkbox2']").click()
driver.find_element(By.CSS_SELECTOR, 'input[class*="success"]').click()

assert 'Success' in driver.find_element(By.CLASS_NAME,'alert-success').text

print('Thank You')
