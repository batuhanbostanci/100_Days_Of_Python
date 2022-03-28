from selenium import webdriver
from selenium.webdriver.common.keys import Keys


chrome_driver_path = "C:\DEVELOPMENT\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://secure-retreat-92358.herokuapp.com/")

search_name = driver.find_element_by_name("fName")
search_last_name = driver.find_element_by_name("lName")
search_mail = driver.find_element_by_name("email")
search_name.send_keys("Batu")
search_last_name.send_keys("Bos")
search_mail.send_keys("denemdenem@gmail.com")

click_button = driver.find_element_by_xpath("/html/body/form/button")
click_button.send_keys(Keys.ENTER)


