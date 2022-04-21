
import requests
from twilio.rest import Client


VIRTUAL_TWILIO_NUMBER = "your virtual twilio number"
VERIFIED_NUMBER = "your own phone number verified with Twilio"

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "YOUR OWN API KEY FROM ALPHAVANTAGE"
NEWS_API_KEY = "YOUR OWN API KEY FROM NEWSAPI"
TWILIO_SID = "YOUR TWILIO ACCOUNT SID"
TWILIO_AUTH_TOKEN = "YOUR TWILIO AUTH TOKEN"


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stock_params={
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "outputsize":"compact",
    "apikey":STOCK_API_KEY,
}

stock_reponse = requests.get(STOCK_ENDPOINT, params=stock_params)
stock_reponse.raise_for_status()
stock_data = stock_reponse.json()["Time Series (Daily)"]
stock_data_list = [value for (key,value) in stock_data.items()]
yesterday = stock_data_list[0]

#Get yesterday's closing stock price
#Get the day before yesterday's closing stock price
bf_yesterday = stock_data_list[1]
price_yesterday  = float(stock_data_list[0]["4. close"])
price_bf_yesterday  = float(stock_data_list[1]["4. close"])

#Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
#Prepare the first part of the message
percent = round((((price_yesterday-price_bf_yesterday)/price_yesterday)*100))
if percent > 0:
    incr_decr = f"TSLA: 🔺{percent}%"
else:
    incr_decr = f"TSLA: 🔻{percent}%"


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

if abs(percent) >= 5:
    news_params={
        "q":COMPANY_NAME,
        "apiKey":NEWS_API_KEY,
    }

    news_reponse = requests.get(NEWS_ENDPOINT, params=news_params)
    news_reponse.raise_for_status()
    news_data = news_reponse.json()
    #Use Python slice operator to create a list that contains the first 3 articles.
    #Create a new list of the first 3 article's
    news_data3 = news_data['articles'][:3] 
    message = ""
    for news in news_data3:
        the_news_title = news['title']
        the_news_descrp = news['description']
        message = f"{incr_decr}\nHeadline: {the_news_title}\nBrief: {the_news_descrp}\n"
    ## STEP 3: Use https://www.twilio.com
    # Send a seperate message with the percentage change and each article's title and description to your phone number. 
        client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
        message = client.messages \
                        .create(
                            body=message,
                            from_=VIRTUAL_TWILIO_NUMBER,
                            to=VERIFIED_NUMBER
                        )

