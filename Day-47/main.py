import requests
from bs4 import BeautifulSoup
import smtplib

URL = "https://www.amazon.com/Apple-MacBook-13-inch-256GB-Storage/dp/B08T4R9D7M/ref=sr_1_4?crid=1T45Y9CB119GO&keywords=macbook+pro+14+inch&qid=1643885866&sprefix=macbook+pro+14+inc%2Caps%2C215&sr=8-4"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.81 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,tr;q=0.8"
   }

response = requests.get(url=URL, headers=header)
soup = BeautifulSoup(response.content, "lxml")
price = soup.find(name="span", class_="a-offscreen").get_text().split("$")

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user="yours", password="Yours")
    connection.sendmail(
        from_addr="Yours",
        to_addrs="To address",
        msg=f"Subject: Price Tracker\n\n Your price is{price[1]}. You can buy it!"
    )




