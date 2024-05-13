import time
from collections import defaultdict
'''
s = "adithya ramakrishna youuuuuuuu"

d = defaultdict(int)
for i in s:
    #if i in d:
    if i.lower() in "aeiou":
        d[i] += 1

print(d)



d={}
names = "hi all how are you"

n = names.split()
for i in n:
    list = []
    for j in n:
        if i[0]==j[0]:
            list.append(i)
            d[i[0]] = list

print(d)



from collections import defaultdict
d = defaultdict(list)
names = "hi all how are you"
l = names.split()

for i in l:
    d[i[0]].append(i)

print(d)


from collections import defaultdict
d = defaultdict(list)
names = "hi all how are yu"
l = names.split()

for i in l:
    d[len(i)].append(i)

print(d)



class A:
    a = 20
    def sum(self):
        c = self.a
        return c


class B(A):
    a = 15
    b = 15

    def sum(self):
        d = self.a + self.b
        return d

ob = B()
print(ob.sum())

'''

'''
class B:
    __age = 15
    def sam(self):
        print("inside one")

    def set_a(self,age):
        self.__age = age
    def get_a(self,age):
        return self.__age


class C(B):

    __age = 20
    def sam(self):
        super().sam()
        print("ss")
        print(self.__age)
        super().get_a(14)

o=C()
o.sam()


try:
    print("abc")

except Exception:
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
#driver = webdriver.Chrome()
driver1 = webdriver.Firefox()

driver1.get("http://omayo.blogspot.com/")
'''
text = driver1.find_element(By.ID, "textbox1")
time.sleep(2)
text.clear()
time.sleep(2)
text.send_keys("adithya")
time.sleep(2)

text.clear()
time.sleep(2)

text.send_keys("Cool")
time.sleep(2)

title = driver1.title
print(title)
print(driver1.current_url)

#driver1.find_element(By.LINK_TEXT,'onlytestingblog').click()

title1 = driver1.title
print(title1)
print(driver1.current_url)

driver1.find_element(By.LINK_TEXT,"Open a popup window").click()

driver1
'''
