from selenium import webdriver

chrome_driver_path = "C:\DEVELOPMENT\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_counts = driver.find_element_by_css_selector("#articlecount a")
print(article_counts.text)


driver.quit()