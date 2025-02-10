import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from datetime import datetime


driver = webdriver.Chrome()
'''
driver.delete_all_cookies()
driver.get("http://13.235.111.246:8051/BankfairWeb/login")
driver.maximize_window()
driver.implicitly_wait(2)
time.sleep(2)
'''

driver.implicitly_wait(2)


class AccountCreation:

    def onboarding(self):

        driver.delete_all_cookies()
        driver.get("http://13.235.111.246:8051/BankfairWeb/login")
        driver.maximize_window()
        # driver.implicitly_wait(2)
        time.sleep(1)
        print("Launched the website")

    def userlogin(self):
        driver.find_element(by=By.XPATH, value="//input[@id = 'loginId']").send_keys('NISARGA')
        driver.find_element(by=By.XPATH, value="//input[@id = 'userPassword']").send_keys('nISARGA@1234567')
        driver.find_element(by=By.XPATH, value="//button[@type = 'submit']").click()
        time.sleep(1)
        print("Logged in")

    def memberdropdown(self):
        # drop = Select(driver.find_element(by=By.XPATH, value="//span[text() = 'Member ']"))
        # drop.select_by_index(1)
        driver.find_element(by=By.XPATH, value="//span[text() = 'Member ']").click()
        time.sleep(1)
        driver.find_element(by=By.XPATH, value="//ul[@class='submenu nav-show']//li[@id='sub1']//a[@class='dropdown-toggle']").click()
        time.sleep(1)
        driver.find_element(by=By.XPATH, value="//li[@id='sub1']//ul[@class='submenu nav-show']//li//a[contains(text(),'Create')]").click()
        time.sleep(1)
        print('went inside member module')

    def nametab(self,title, fname, sname, dob, gender, maiden, nick,ptype, idnumber, isdate, exdate,country):
        titledrop = Select(driver.find_element(by=By.XPATH, value="//select[@id='nameTitle']"))
        titledrop.select_by_index(title)
        print(f'selected title is {title}')
        driver.find_element(by=By.XPATH, value="//input[@id='firstName']").send_keys(fname)
        print(f'firstname is {fname}')
        driver.find_element(by=By.XPATH, value="//input[@id='lastName']").send_keys(sname)
        print(f'lastname is {sname}')

        if isinstance(dob, datetime):
            dob = dob.strftime('%d-%b-%Y')
        elif isinstance(dob, str):
            try:
                dob = datetime.strptime(dob, '%d-%b-%Y').strftime('%d-%b-%Y')
            except ValueError:
                print(f"Invalid date format for DOB in row:- {dob}")
                return

        abc = driver.find_element(by=By.XPATH, value="//input[@id='dateOfBirth']") # .send_keys(str(dob))
        abc.send_keys(str(dob))
        abc.send_keys(Keys.ENTER)
        print(f'dob is {dob}')
        # time.sleep(2)
        genderdrop = Select(driver.find_element(by=By.XPATH, value="//select[@id='gender']"))
        genderdrop.select_by_visible_text(gender)
        print(f'gender is {gender}')
        driver.find_element(by=By.XPATH, value="//input[@id='maidenName']").send_keys(maiden)
        print(f'maiden name is {maiden}')
        driver.find_element(by=By.XPATH, value="//input[@id='nickNameorAlias']").send_keys(nick)
        print(f'nickname is {nick}')
        idtypedrop = Select(driver.find_element(by=By.XPATH, value="//select[@id='passportIssuedAt']"))
        idtypedrop.select_by_index(ptype)
        print(f'id type is {ptype}')
        driver.find_element(by=By.XPATH, value="//input[@id='passportNo' or @name='passportNo']").send_keys(idnumber)
        print(f'id number is {idnumber}')

        if isinstance(isdate, datetime):
            isdate = isdate.strftime('%d-%b-%Y')
        elif isinstance(isdate, str):
            try:
                isdate = datetime.strptime(dob, '%d-%b-%Y').strftime('%d-%b-%Y')
            except ValueError:
                print(f"Invalid date format for DOB in row:- {isdate}")
                return

        abc = driver.find_element(by=By.ID, value='issueDt') # .send_keys(isdate)
        abc.send_keys(isdate)
        abc.send_keys(Keys.ENTER)
        print(f'issue date is {isdate}')
        # time.sleep(2)

        if isinstance(exdate, datetime):
            exdate = exdate.strftime('%d-%b-%Y')
        elif isinstance(exdate, str):
            try:
                exdate = datetime.strptime(dob, '%d-%b-%Y').strftime('%d-%b-%Y')
            except ValueError:
                print(f"Invalid date format for DOB in row:- {exdate}")
                return

        abc = driver.find_element(by=By.ID, value='expiryDt') # .send_keys(exdate)
        abc.send_keys(exdate)
        abc.send_keys(Keys.ENTER)
        print(f'expire date is {exdate}')
        # time.sleep(2)
        countrydrop = Select(driver.find_element(by=By.ID, value='primaryCountryofIssue'))
        countrydrop.select_by_visible_text(country)
        print(f'country is {country}')

        time.sleep(1)

    def communicationtab(self, country, state, city, zipcode):
        driver.find_element(by=By.XPATH, value="//a[text()='Communication']").click()
        print("went inside communication module")
        driver.find_element(by=By.XPATH, value="//input[@id='searchCountryList1']").send_keys(country)
        print(f'country is {country}')
        driver.find_element(by=By.XPATH, value="//input[@id='searchDistrict1']").send_keys(state)
        print(f'state if {state}')
        driver.find_element(by=By.XPATH, value="//input[@id='searchCity1']").send_keys(city)
        print(f'city is {city}')
        driver.find_element(by=By.XPATH, value="//input[@id='presentAddressPostalCode']").send_keys(zipcode)
        print(f'zipcode is {zipcode}')

    def controltab(self, person):
        driver.find_element(by=By.XPATH, value="//a[text()='Control']").click()
        print('went inside control module')
        hrcudrop = Select(driver.find_element(by=By.XPATH, value="//select[@id='howPersonLearn']"))
        hrcudrop.select_by_index(person)
        print(f'how person learnt is {person}')
        driver.find_element(by=By.XPATH, value="//button[@id='SubmitBtn']").click()
        time.sleep(1)
        print('clicked on submit button')
        driver.find_element(by=By.XPATH,value="(//div[@class='ui-dialog-buttonset'] //button[text()='Yes'])[1]").click()
        print('clicked on "Yes" in popup')

    '''
    def verification(self):
        try:
            ver = driver.find_element("xpath", "//div[normalize-space()='Member Added Successfully!']//div[@id='SatusMsg']")
            status = ver.text
            if "success" in status:
                print("Member is added successfully")
                return True

        except Exception as e:
            print("Member is not added, please re-verify once")
            # print(e)
            return False
'''
    def memberid(self):

        memberidnum = driver.find_element(by=By.XPATH, value="//input[@id='cif']").get_attribute("value")
        return memberidnum


