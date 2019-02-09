from selenium import webdriver

browser='ie'

if browser=='chrome':
    driver=webdriver.Chrome(executable_path="C:/Users/nagen/PycharmProjects/5_Class/Drivers/chromedriver.exe")
elif browser=='firefox':
    driver=webdriver.Firefox(executable_path="C:/Users/nagen/PycharmProjects/5_Class/Drivers/geckodriver.exe")
elif browser=='ie':
    driver=webdriver.Ie(executable_path="C:/Users/nagen/PycharmProjects/5_Class/Drivers/IEDriverServer.exe")
else:
    print("enter valid browser name")
driver.get("http://facebook.com")
driver.maximize_window()

driver.find_element_by_id("email").send_keys("FakeUser")
driver.find_element_by_id("pass").send_keys("FakePwd")
driver.find_element_by_id("u_0_2").click()