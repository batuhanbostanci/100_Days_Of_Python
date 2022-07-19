from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

chrome_driver_path = "C:\DEVELOPMENT\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://twitter.com/login")


time.sleep(2)

username = driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div[2]/div/input')
username.send_keys("******") # This is your twitter username
username.send_keys(Keys.ENTER)


time.sleep(1)
password = driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
password.send_keys("*******") # This is your twitter account
password.send_keys(Keys.ENTER)

time.sleep(1)

driver.get('https://twitter.com/Cristiano') # This is the account which is going to be

time.sleep(2)

followers = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div/div/div[5]/div[2]/a/span[1]/span')
followers.click()

time.sleep(1)

data_username = []



for i in range(1, 51): # This for loop takes the user name of the account
    link = f'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div[{i}]/div/div/div/div[2]/div/div[1]/div/div[2]/div/a'
    try:
        users = driver.find_element_by_xpath(link)
        # print(f"{i: } {users.text}")

        data_username.append(users.text)

    except NoSuchElementException:
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(1)

final_data=[]

for user in data_username: # This for loop goes every follower and takes their information

    link = f"https://twitter.com/{user}"
    driver.get(link)
    time.sleep(2)

    full_name = ""
    description = ""
    website = ""
    birthday = ""
    joined_time = ""
    number_of_followers = ""
    number_of_following = ""

    location = ""
    birth_date = ""
    join_date = ""
    link_address=""
    controller =3;
    try:
        full_name = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[1]/div/div/span[1]/span').text
    except NoSuchElementException:
        full_name = "No Information"

    try:

        description = driver.find_element_by_css_selector(".r-1ifxtd0 .r-1adg3ll .css-1dbjc4n .r-1nao33i").text
        controller = controller + 1
    except NoSuchElementException:
        description = "No Information"


    try:
        website = driver.find_element_by_css_selector(".r-1ifxtd0 .r-1adg3ll .r-1nao33i a").text
    except NoSuchElementException:
        website = "No WebSite Information"

    info_controller = 1;
    try:
        link = f'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div/div/div[{controller}]/div/span[{info_controller}]'
        location = driver.find_element_by_xpath(link).text
        info_controller = info_controller + 1

    except NoSuchElementException:
        location = "No Location Information"


    try:
        link = f'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div/div/div[{controller}]/div/span[{info_controller}]'
        birth_date = driver.find_element_by_xpath(link).text
        info_controller = info_controller + 1

    except NoSuchElementException:
        birth_date = "No Birth Information"


    try:

        link = f'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div/div/div[{controller}]/div/a]'
        link_address = driver.find_element_by_xpath(link)


    except NoSuchElementException:
        link_address = "No Link Adrress Information"


    try:

        link = f'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div/div/div[{controller}]/div/span[{info_controller}]'
        join_date = driver.find_element_by_xpath(link).text
        info_controller = info_controller + 1

    except NoSuchElementException:
        join_date = "No Join Date Information"


    try:
        number_of_followers = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div/div/div[5]/div[2]/a/span[1]/span').text
        number_of_followers = number_of_followers + " Followers"
    except NoSuchElementException:
        number_of_followers = "No Information"
    try:
        number_of_following = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div/div/div[5]/div[1]/a/span[1]/span').text
        number_of_following = number_of_following + " Following"
    except NoSuchElementException:
        number_of_following = "No Information"

    row_data = { # Dictionary for informations
        "Username": user,
        "Displayed":full_name,
        "Description": description,
        "Location":location,
        "Number of Followers":number_of_followers,
        "Number of Following": number_of_following,
        "Birthday": birth_date,
        "Joined Time": join_date,
        "Website": website,
        "L50_favorites": "No Info",
        "L50_retweets": "No Info",
        "L50_replies": "No Info"
    }
    final_data.append(row_data)
    print(row_data)

print(final_data)