import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("http://175.100.150.82/")
driver.maximize_window()
driver.implicitly_wait(5)


class Attendance:

    def login(self):
        driver.find_element("xpath", "//input[@name='name']").send_keys('harsha.ad')
        driver.find_element("xpath", "//input[@name='pass']").send_keys('12345')
        driver.find_element("xpath", "//input[@name='op']").click()
        print("Logged in successfully")
        time.sleep(2)

    def add_attendance(self):
        driver.find_element("xpath", "//a[text()='Add attendance']").click()
        time.sleep(2)

    def month_dropdown(self):
        # click on Month dropdown
        driver.find_element('xpath', "//div[@id='edit_field_month_und_0_value_month_chosen']").click()
        print("Clicked on Month Dropdown")

        # Enter the Month value in the search box
        month = driver.find_element("xpath", "//div[@id='edit_field_month_und_0_value_month_chosen']"
                                             "//div[@class='chosen-drop']//input[@type='text']")
        month.send_keys("Dec")
        print(f"Entered value in the Month search field is December")
        time.sleep(1)

        # click on the suggestion
        month.send_keys(Keys.ENTER)
        #driver.find_element("xpath", "//*[@id='edit_field_month_und_0_value_month_chosen']/div/ul/li[1]").click()
        print("Clicked on the Suggested Month option")
        time.sleep(2)

    def year_dropdown(self):
        # click on Year dropdown
        driver.find_element("xpath", "//div[@id='edit_field_month_und_0_value_year_chosen']").click()
        print("Clicked on Year Dropdown")

        # Enter the Year value in the search box
        year = driver.find_element("xpath", "//div[@id='edit_field_month_und_0_value_year_chosen'] "
                                            "//input[@class='chosen-search-input']")
        year.send_keys('2023')
        print("Entered value in the Year search field is 2023")
        time.sleep(1)

        # click on the suggestion
        #driver.find_element("xpath", "//*[@id='edit_field_month_und_0_value_year_chosen']/div/ul/li[2]").click()
        year.send_keys(Keys.ENTER)
        print("Clicked on the Suggested Year option")
        time.sleep(2)

    def worked_days(self, value):
        # click on Worked days
        w_days = driver.find_element('xpath', "//input[@id='edit-field-working-days-und-0-value']")
        w_days.send_keys(value)
        print(f"Entered Worked days value is {value}")

    def leaves(self, value):
        # click on Worked days
        l_days = driver.find_element("xpath", "//input[@id='edit-field-leaves-taken-und-0-value']")
        l_days.send_keys(value)
        print(f"Entered leaves days value is {value}")

    def project_dropdown(self, value):
        # click on Project dropdown
        driver.find_element("xpath", "//div[@id='edit_field_project_attend_und_chosen']").click()
        print("Clicked on Project Dropdown")

        # Enter the Project value in the search box
        project_dd = driver.find_element("xpath", "//div[@id='edit_field_project_attend_und_chosen'] "
                                                  "//input[@class='chosen-search-input']")
        project_dd.send_keys(value)
        print(f"Entered value in the Project search field is {value}")
        time.sleep(1)

        # click on the suggestion
        #driver.find_element("xpath", "//*[@id='edit_field_project_attend_und_chosen']/div/ul/li[1]").click()
        project_dd.send_keys(Keys.ENTER)
        print("Clicked on the Suggested project option")
        time.sleep(2)

    def employee_id(self, value):
        # click on the authoring information tab
        driver.find_element("xpath", "//span[normalize-space()='By harsha.ad']").click()
        print("Clicked on the authoring information tab")

        # clear the existing name
        emp_id = driver.find_element("xpath", "//input[@id='edit-name']")
        emp_id.clear()
        print("Cleared the name")

        # Enter employee id
        emp_id.send_keys(value)
        print(f"Entered employee Id is {value}")

        # click on the submit button
        driver.find_element("xpath", "//*[@id='edit-submit']").click()
        print("Clicked on the Submit button")
        time.sleep(2)

    def verification(self):
        try:
            ver = driver.find_element("xpath", "//div[@class='messages status']")
            status = ver.text
            if "has been created" in status:
                print("Attendance is added successfully")
                return True

        except Exception as e:
            print("Attendance is not added, please re-verify once")
            #print(e)
            return False

    def get_projectsname(self):
        self.add_attendance()
        driver.find_element("xpath", "//div[@id='edit_field_project_attend_und_chosen']").click()
        projects = (driver.find_elements("xpath", "//li[contains(@class,'active-result')]"))

        pros = []
        for i in projects:
            a = i.text
            pros.append(a)

        print(pros)
