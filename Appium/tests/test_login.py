import pytest
from Appium.pages.login_page import LoginPage
from Appium.pages.home_page import HomePage
from Appium.utils.driver_factory import init_driver
import json
import os


@pytest.fixture(scope="class")
def setup(request):
    print("Initializing the driver...")
    driver = init_driver()
    request.cls.driver = driver
    yield
    print("Quitting the driver...")
    driver.quit()


@pytest.mark.usefixtures("setup")
class TestLogin:
    driver = None

    def test_login_and_home_navigation(self):
        driver = init_driver()
        print(f"Driver initialized: {driver}")
        print("Test: Login and Home Navigation started...")

        # Initialize the page objects
        login_page = LoginPage(self.driver)
        home_page = HomePage(self.driver)

        # Get the absolute path to the JSON data file
        data_file_path = r'D:\TestYantra files\PycharmProjects\pythonProject1\Appium\data\test_data.json'
        print(f"Loading test data from: {data_file_path}")

        # Load test data from the JSON file
        with open(data_file_path, 'r') as data_file:
            data = json.load(data_file)

        # Extract login credentials from the JSON file
        email = data['login']['email']
        password = data['login']['password']
        print(f"Test data loaded: Email = {email}, Password = {password}")

        # Perform the login
        print("Performing login...")
        login_page.login(email, password)

        # Handle permissions and navigate home
        print("Handling permissions and navigating home...")
        home_page.permission()
        # home_page.navigate_home()

        print("Test: Login and Home Navigation completed.")
