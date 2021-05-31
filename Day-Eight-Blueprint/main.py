import os
import csv
import requests
from bs4 import BeautifulSoup
from save_extract import save_file, brand_info
from super_brand import brand

os.system("clear")

def brand_info(link):
  result = requests.get(link)
  soup = BeautifulSoup(result.text,'html.parser')
  soup = soup.find('div',{'id':'NormalInfo'})
  jobs = []

  place = []
  title = []
  time = []
  pay = []
  date = []
  try:
    for loca in soup.find_all('td',{'class':'local'}):
      place.append(loca.get_text().replace(u'\xa0', u' '))
    for inf in soup.find_all('span',{'class':'company'}):
      title.append(inf.get_text().replace(u'\xa0', u' '))
    for w_t in soup.find_all('td',{'class':'data'}):
      time.append(w_t.get_text())
    for pa in soup.find_all('td',{'class':'pay'}):
      pay.append(pa.get_text())
    for reg in soup.find_all('td',{'class':'regDate'}):
      date.append(reg.get_text())

    for i in range(len(place)):
      jobs.append([place[i],title[i],time[i],pay[i],date[i]])
  except:
    jobs = ['No Data','No Data','No Data','No Data','No Data']
  return jobs

link ='http://gs25.alba.co.kr/job/brand/?page=1&pagesize=3000'
print(brand_info(link))

