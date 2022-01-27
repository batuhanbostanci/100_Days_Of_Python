from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")

yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")

articles = soup.find_all(name="a", class_="titlelink")
article_texts = []
article_links = []
for article_tag in articles:
    article_text = article_tag.getText()
    article_link = article_tag.get("href")
    article_links.append(article_link)
    article_texts.append(article_text)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

index_of_highest = article_upvotes.index(max(article_upvotes))

print(article_texts[index_of_highest])
print(article_links[index_of_highest])
print(article_upvotes[index_of_highest])


# with open("website.html", encoding="utf8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
#
#
# # print(soup.title)
# # print(soup.title.string)
#
# all_anchor_tags = soup.find_all(name="a")
# # print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)
#
#
# company_url = soup.select_one(selector="p a")
# print(company_url)
#
# headings = soup.select(".heading")
# print(headings)
