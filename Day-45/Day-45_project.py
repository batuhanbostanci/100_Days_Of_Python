import requests
from bs4 import BeautifulSoup


response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
web_text = response.text

soup = BeautifulSoup(web_text, "html.parser")

title_of_films = soup.find_all(name="h3", class_="title")

name_list = []
for title in title_of_films:
    name_list.append(title.text)

with open("Top_100_films.txt", "w") as file:
    for item in name_list:
        file.write(f"{item}\n")