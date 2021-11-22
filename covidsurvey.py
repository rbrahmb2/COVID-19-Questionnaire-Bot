
import selenium
from selenium import webdriver
import time

driver = webdriver.Chrome("C:/Users/PC/Desktop/chromedriver_win32/chromedriver.exe")

#change the path below
#possibly may have to configure version of chrome or driver version
driver.get('https://www.uwo.ca/coronavirus/questionnaire.html')

driver.find_element_by_class_name("btn.btn-primary").click()

#time.sleep(5)

#id_box = driver.find_element_by_xpath('/html/body/div[3]/div/div/form/fieldset/div[1]/input')
#pass_box = driver.find_element_by_xpath('/html/body/div[3]/div/di  v/form/fieldset/div[2]/input')

driver.switch_to_window(driver.window_handles[1])
time.sleep(1)
id_box = driver.find_element_by_name('j_username')
pass_box = driver.find_element_by_name('j_password')

id_box.send_keys('Enter Username Here')
pass_box.send_keys("Enter Password Here")


driver.find_element_by_class_name('adt-primaryAction.adt-btn.adt-large').click()

time.sleep(1)

driver.switch_to_window(driver.window_handles[1])

driver.find_element_by_id('QID27-4-label').click()

driver.find_element_by_id('NextButton').click()

driver.switch_to_window(driver.window_handles[1])

time.sleep(1)

driver.find_element_by_id('QID11-4-label').click()

driver.find_element_by_id('NextButton').click()

driver.switch_to_window(driver.window_handles[1])

time.sleep(1)

driver.find_element_by_id('QID4-8-label').click()

driver.find_element_by_id('QID30-1-label').click()

driver.find_element_by_id('QID29-1-label').click()

driver.find_element_by_id('QID33-1-label').click()

driver.find_element_by_id('QID34-1-label').click()

driver.find_element_by_id('NextButton').click()



