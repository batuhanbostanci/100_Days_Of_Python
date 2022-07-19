from selenium import webdriver

chrome_driver_path = "C:\DEVELOPMENT\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://python.org")

# price = driver.find_element_by_class_name("a-price-whole")
# print(price.text)

# search_bar = driver.find_element_by_name("q")
# print(search_bar)

# logo = driver.find_element_by_class_name("python-logo")
# print(logo.size)

# documentation_link = driver.find_element_by_xpath("//*[@id='content']/div/section/div[2]/div[3]/p[2]/a")
# print(documentation_link.text)

event_times = driver.find_elements_by_css_selector(".event-widget time")
event_names = driver.find_elements_by_css_selector(".event-widget li a")
events= {}


for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text,
    }
print(events)
