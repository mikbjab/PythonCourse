import bs4
import requests

# Web scraping reddita można wykorzystać do automatycznego śledzenia wiadomości (typu subreddit politics) oraz ich popularności (liczba komentarzy)

response=requests.get("https://www.reddit.com/svc/shreddit/community-more-posts/hot/?after=dDNfMTh3N2FpaA%3D%3D&t=DAY&name=politics&adDistance=2&feedLength=4")
soup_example=bs4.BeautifulSoup(response.text,"html.parser")
article_list=soup_example.find_all("article",class_="m-0")
print(len(article_list))
for article in article_list:
    print("Tytuł postu: "+article.a["aria-label"])
    print("Link: https://www.reddit.com"+article.a["href"])
    print("Link zewnętrzny: "+article.contents[1]["content-href"])
    print("Data stworzenia: "+article.contents[1]["created-timestamp"])
    print("Liczba komentarzy: "+article.contents[1]["comment-count"])