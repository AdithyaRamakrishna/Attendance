from appium import webdriver
import json


def init_driver():
    print("inside init_driver")
    with open(r'D:\TestYantra files\PycharmProjects\pythonProject1\Appium\config\capabilities.json',
              'r') as config_file:
        data = json.load(config_file)

        capabilities = data.get('capabilities')

        if not capabilities:
            raise ValueError("Capabilities are not defined in the variables file.")
        print(capabilities)

    # Remove "appium:" prefixes in the dictionary keys if they're causing issues.
    capabilities_cleaned = {key.replace('appium:', ''): value for key, value in capabilities.items()}

    print("Cleaned Capabilities:", capabilities_cleaned)

    # Pass the cleaned capabilities directly to the WebDriver.
    return webdriver.Remote("http://127.0.0.1:4723/wd/hub", capabilities_cleaned)


# Test driver initialization
