import requests
from bs4 import BeautifulSoup



response=requests.get("https://www.fmkorea.com/coin")


html=response.text
soup=BeautifulSoup(html,'html.parser')
links=soup.select(".title hotdeal_var8")


for link in links:
    title=link.text
    
    print(title)