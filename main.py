import requests
import datetime as dt
import math

STOCK_NAME = "Apple&"
COMPANY_NAME = "Reliance Industries"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

Alpha_api_key="XQ6OWVCC1QOI3N12"
News_api_key="2b1745a888e84ebcaeb50f1f2c92e9a8"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
parameters1={
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey":Alpha_api_key
}

parameters2={
    "qInTitle":STOCK_NAME,
    "from":2024-7-26,
    "sortBy":"popularity",
    "apiKey":News_api_key
}


# recived_Stock=requests.get(STOCK_ENDPOINT,params=parameters1)
# data=recived_Stock.json()["Time Series (Daily)"]
# #print(data["Time Series (Daily)"]["2024-07-26"])
# data_list=[(value) for (key,value) in data.items()]
# print(data_list[0]["4. close"])

recived_news=requests.get(NEWS_ENDPOINT,params=parameters2)
news_data=recived_news.json()
articles=news_data["articles"]
top10=[article for article in articles if article.get("title") != "[Removed]"]
print(f"{top10[:1]}\n\n\n {top10[1:2]}\n\n\n {top10[2:3]}\n ")




# last_day=data_list[0]["4. close"]
# day_before=data_list[1]["4. close"]

# print(last_day)
# print(day_before)
# Price_Diff=abs(float(day_before)-float(last_day))
# print(Price_Diff)

# percentage_change=round(((Price_Diff/float(day_before))*100),2)
# print(f"Percentage Change:{percentage_change}%")

# if percentage_change>1:
#     print("Get News")
# else:
#     pass


#TODO 2. - Get the day before yesterday's closing stock price

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

