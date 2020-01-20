from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

path = 'C:/Users/nelso/Documents/Data Science/Python/Scripts/Firefox Scraper/geckodriver.exe'
driver = Firefox(executable_path=path)
driver.get('https://www.google.com')

que=driver.find_element_by_xpath("//input[@name='q']")
sleep(5)
que.send_keys("waffles")
sleep(5)
button = driver.find_element_by_xpath("//input[@value='Google Search']")
button.click()

sleep(5)
mydata = []
webitem = driver.find_elements_by_class_name('LC20lb')

for item in webitem:
    mydata.append(item.text)

driver.quit()

print(mydata)
