from selenium import webdriver
from selenium.webdriver.common.keys import Keys
##driver = webdriver.Chrome(executable_path="C:/Utils/chromedriver_win32/chromedriver.exe")
driver=webdriver.Chrome(executable_path="C:/Drivers/chromedriver_win32/chromedriver.exe")
driver.get("http://newtours.demoaut.com/")
print(driver.title)
##driver.close()
