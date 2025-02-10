import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from datetime import datetime


driver = webdriver.Chrome()

driver.implicitly_wait(2)


class AccountCreation:

    def onboarding(self):

        driver.delete_all_cookies()
        driver.get("http://13.235.111.246:8051/BankfairWeb/login")
        driver.maximize_window()
        # driver.implicitly_wait(2)
        time.sleep(2)
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

    def nametab(self):
        titledrop = Select(driver.find_element(by=By.XPATH, value="//select[@id='nameTitle']"))
        titledrop.select_by_index(1)
        # print(f'selected title is {title}')
        driver.find_element(by=By.XPATH, value="//input[@id='firstName']").send_keys('Adithya')
       # print(f'firstname is {fname}')
        driver.find_element(by=By.XPATH, value="//input[@id='lastName']").send_keys('Adhi')
       # print(f'lastname is {sname}')
        abc = driver.find_element(by=By.XPATH, value="//input[@id='dateOfBirth']") # .send_keys(str(dob))
        abc.send_keys('15-Jan-1965')
        abc.send_keys(Keys.ENTER)
       # print(f'dob is {dob}')
        # time.sleep(2)
        genderdrop = Select(driver.find_element(by=By.XPATH, value="//select[@id='gender']"))
        genderdrop.select_by_visible_text('Male')
       # print(f'gender is {gender}')
        driver.find_element(by=By.XPATH, value="//input[@id='maidenName']").send_keys('Sash')
      #  print(f'maiden name is {maiden}')
        driver.find_element(by=By.XPATH, value="//input[@id='nickNameorAlias']").send_keys('Adi')
      #  print(f'nickname is {nick}')
        idtypedrop = Select(driver.find_element(by=By.XPATH, value="//select[@id='passportIssuedAt']"))
        idtypedrop.select_by_index(2)
       # print(f'id type is {ptype}')
        driver.find_element(by=By.XPATH, value="//input[@id='passportNo' or @name='passportNo']").send_keys('PJJO45714')
      #  print(f'id number is {idnumber}')
        abc = driver.find_element(by=By.ID, value='issueDt') # .send_keys(isdate)
        abc.send_keys('15-Jul-2010')
        abc.send_keys(Keys.ENTER)
       # print(f'issue date is {isdate}')
        # time.sleep(2)
        abc = driver.find_element(by=By.ID, value='expiryDt') # .send_keys(exdate)
        abc.send_keys('20-Sep-2029')
        abc.send_keys(Keys.ENTER)
      #  print(f'expire date is {exdate}')
        # time.sleep(2)
        countrydrop = Select(driver.find_element(by=By.ID, value='primaryCountryofIssue'))
        countrydrop.select_by_visible_text('Belize')
       # print(f'country is {country}')

        time.sleep(2)

    def communicationtab(self):
        driver.find_element(by=By.XPATH, value="//a[text()='Communication']").click()
        print("went inside communication module")
        driver.find_element(by=By.XPATH, value="//input[@id='searchCountryList1']").send_keys('Belize')
     #   print(f'country is {country}')
        driver.find_element(by=By.XPATH, value="//input[@id='searchDistrict1']").send_keys('Corozol')
     #   print(f'state if {state}')
        driver.find_element(by=By.XPATH, value="//input[@id='searchCity1']").send_keys('Calcutta')
     #   print(f'city is {city}')
        driver.find_element(by=By.XPATH, value="//input[@id='presentAddressPostalCode']").send_keys(80201)
     #   print(f'zipcode is {zipcode}')

    def controltab(self):
        driver.find_element(by=By.XPATH, value="//a[text()='Control']").click()
        print('went inside control module')
        hrcudrop = Select(driver.find_element(by=By.XPATH, value="//select[@id='howPersonLearn']"))
        hrcudrop.select_by_index(1)
     #   print(f'how person learnt is {person}')

        driver.find_element(by=By.XPATH, value="//button[@id='SubmitBtn']").click()
        time.sleep(1)
        print('clicked on submit button')
        driver.find_element(by=By.XPATH,value="(//div[@class='ui-dialog-buttonset'] //button[text()='Yes'])[1]").click()
        print('clicked on "Yes" in popup')
        time.sleep(10)

    def verification(self):
        driver.find_element("xpath", "//div[normalize-space()='Member Added Successfully!']//div[@id='SatusMsg']")
        print("Member is added successfully")

    def memberid(self):

        memberidnum = driver.find_element(by=By.XPATH, value="//input[@id='cif']").get_attribute("value")
        print(f'member is {memberidnum}')
        return memberidnum


NewUser = AccountCreation()
NewUser.onboarding()
NewUser.userlogin()
NewUser.memberdropdown()
NewUser.nametab()
NewUser.communicationtab()
NewUser.controltab()
NewUser.verification()
NewUser.memberid()

if NewUser.verification():
    memberidnum = NewUser.memberid()
    print(f'member id is {memberidnum}')

else:
    print('member ID is not created')
