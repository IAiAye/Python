import requests
from bs4 import BeautifulSoup

alba_url = "http://www.alba.co.kr"

def brand():
  result = requests.get(alba_url)
  soup = BeautifulSoup(result.text,'html.parser')
  brands = soup.find_all('li',{'class':'impact'})
  names_n_links = {}
  for brand in brands:
    name = brand.find('span',{'class','company'}).string
    link = brand.find('a')['href']
    names_n_links[name] = link
  return names_n_links