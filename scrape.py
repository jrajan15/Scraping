from bs4 import BeautifulSoup
import requests

url = "https://developer.android.com/training/basics/firstapp/creating-project"
response = requests.get(url)
data = response.text
soup = BeautifulSoup(data, 'html.parser')
tags = soup.find_all('a')
##for tag in tags:
##    print(tag.get('href'))
titles = soup.find_all("a", {"class":"result-title"})
for title in titles:
    print(title.text)

addresses = soup.find_all("span",{"class":"result-hood"})
for address in addresses:
    print(address.text)

