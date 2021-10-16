import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY_STOCK_PRICE = "******"
API_KEY_GET_NEWS = "*******"

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": API_KEY_STOCK_PRICE
}
URL_FOR_PRICING = 'https://www.alphavantage.co/query'
response = requests.get(url=URL_FOR_PRICING, params=parameters)
response.raise_for_status()

data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]["4. close"]
day_before_yesterday_data = data_list[1]["4. close"]

differance = abs(float(yesterday_data) - float(day_before_yesterday_data))
percentage = (differance/float(yesterday_data)) * 100

if percentage < 5:
    URL_FOR_NEWS = "https://newsapi.org/v2/everything"
    parameters_for_news = {
        "q": COMPANY_NAME,
        "apikey": API_KEY_GET_NEWS
    }
    response_for_news = requests.get(url=URL_FOR_NEWS, params=parameters_for_news)
    response_for_news.raise_for_status()
    data_for_news = response_for_news.json()["articles"]
    data_for_news_first_three = data_for_news[:3]

    formatted_articles = [f"Headline:{article['title']}. \n Brief:{article['description']}" for article in data_for_news_first_three]

    for news in formatted_articles:
        print(news + "\n")


