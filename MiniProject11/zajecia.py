import bs4
import requests


with open("site.html","r") as file_html:
    file=file_html.read()

soup=bs4.BeautifulSoup(file,"html.parser")

response=requests.get("https://example.com")
soup_example=bs4.BeautifulSoup(response.text,"html.parser")
naglowki=soup_example.find_all("h1")
print("Nagłówki:")
print([naglowek.string for naglowek in naglowki])
paragrafy=soup_example.find_all("p")
print("Paragrafy:")
print([p.string for p in paragrafy])
print("Linki:")
all_links = soup.select('a')
print([link["href"] for link in all_links])