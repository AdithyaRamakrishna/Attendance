from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WaitUtils:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

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
