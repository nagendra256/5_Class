
from selenium import webdriver

browser='chrome'

if browser=='chrome':
    driver=webdriver.Chrome(executable_path="C:/Users/nagen/PycharmProjects/5_Class/Drivers/chromedriver.exe")
elif browser=='firefox':
    driver=webdriver.Firefox(executable_path="C:/Users/nagen/PycharmProjects/5_Class/Drivers/geckodriver.exe")
elif browser=='ie':
    driver=webdriver.Ie(executable_path="C:/Users/nagen/PycharmProjects/5_Class/Drivers/IEDriverServer.exe")
else:
    print("enter valid browser name")
driver.get("http://makemytrip.com")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element_by_id("header_tab_hotels").click()
driver.find_element_by_id("header_tab_holidays").click()
driver.back()
driver.forward()