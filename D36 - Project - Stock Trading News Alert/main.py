import requests
from twilio.rest import Client

VIRTUAL_TWILIO_NUMBER = "MY TWILIO NUMBER"
VERIFIED_NUMBER = "MY TEL NUMBER"

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantae.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everythin"

STOCK_API_KEY = "MY OWN API KEY FROM ALPHAVANTAGE"
NEWS_API_KEY = "MY OWN API KEY FROM NEWSAPI"
TWILIO_SID = "MY TWILIO ACCOUNT SID"
TWILIO_AUTH_TOKEN = "MY TWILIO AUTH TOKEN"

# STEP01: Use https://www.alphavantage.co/documentation/#daily
# When stock price increases/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# Get yesterday's closing stock price
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

# Get the day before yesterday's closing stock price
dby_data = data_list[1]
dby_closing_price = dby_data["4. close"]
print(dby_closing_price)

# Find the positive differences between 1 and 2. e.g. 40 - 20 = - 20, but positive difference is 20. Hint https://www.w3schools.com/python/ref_func_abs.asp
difference = float(yesterday_closing_price) - float(dby_closing_price)
up_down = None
if difference > 0:
    up_down = "⬆️"
else:
    up_down = "⬇️"

# Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percent = round((difference / float(yesterday_closing_price)) * 100)
print(diff_percent)

# STEP02: Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

# Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
# If difference percentage is greater than 5 then print ("Get News").
if abs(diff_percent) > 1:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]

    # Use python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    three_articles = articles[:3]
    print(three_articles)

    # STEP03: Use Twilio to send a separate message with each article's title and description to my phone number.
    # Create a new list of the first 3 article's headline and description using list comprehension.
    formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
    print(formatted_articles)
    # Send each article as a separate message via Twilio
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_=VIRTUAL_TWILIO_NUMBER,
            to=VERIFIED_NUMBER
        )
