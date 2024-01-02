import bs4
import requests
import pandas as pd

response=requests.get("https://www.mimuw.edu.pl/")
soup_example=bs4.BeautifulSoup(response.text,"html.parser")
calendar=soup_example.find(id="block-views-calendar-block")
list_of_events=calendar.find_all("li")
result=[]

for event in list_of_events:
    temp_date=event.contents[0].get_text()
    temp_title=event.contents[1].get_text() if event.contents[1].get_text()!="TBA" else event.contents[4].get_text()
    temp_link=event.contents[1].next_element.get("href")
    result.append({"tytul":temp_title,"data":temp_date,"link":"https://www.mimuw.edu.pl"+temp_link})

data=pd.DataFrame.from_records(result)
data.to_csv("wydarzenia.csv")
print(data.sample(5))
