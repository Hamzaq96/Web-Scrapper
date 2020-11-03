import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get("https://forecast.weather.gov/MapClick.php?lat=38.8904&lon=-77.032#.X59IMq5OlH4")

soup = BeautifulSoup(page.content, 'html.parser')

#Find the parent tag first.
seven_day = soup.find(id="seven-day-forecast")

# print(seven_day)

# forecast_items = seven_day.find_all(class_="tombstone-container")
# tonight = forecast_items[1]

#Select the child tag.
period_tags = seven_day.select(".tombstone-container .period-name")
# print(tonight.prettify())

#Extracting the content from the tags.
periods = [pt.get_text() for pt in period_tags]

short_desc = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
descs = [d["title"] for d in seven_day.select(".tombstone-container img")]

# period = tonight.find(class_="period-name").get_text()
# short_desc = tonight.find(class_="short-desc").get_text()
# temp = tonight.find(class_="temp").get_text()

# img = tonight.find("img")
# desc = img['title']


#DataFrame is an object that can store tabular data
weather = pd.DataFrame({
    "period": periods,
    "short_desc": short_desc,
    "temp": temps,
    "desc": descs
})

#Print to check the data collected is correct.
# print(descs)
# # print(periods)
# print(short_desc)
# print(temps)

print(weather)