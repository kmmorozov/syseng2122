from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()

driver.get("https://accounts.google.com/ServiceLogin/identifier?hl=ru&passive=true&continue=https%3A%2F%2Fwww.google.com%2F&flowName=GlifWebSignIn&flowEntry=AddSession")

elem = driver.find_element_by_name("identifier")
elem.send_keys("stefanbelgrade1389@gmail.com")

elem.submit()
 
elem2=driver.find_element_by_id("identifierNext")
elem2.click()

sleep(3)

driver.switch_to_window

elem3=driver.find_element_by_name("password")
elem3.send_keys("123qaz123qaz")

elem4=driver.find_element_by_id("passwordNext")
elem4.click()