import csv
import requests
from bs4 import BeautifulSoup

def save_file(names_n_links):
  for name, link in names_n_links.items():
    name = str(name)
    ban = ['/','?','%','*',':','|','\"',"\\","<",">",'.']
    for character in ban:
      if name.find(character) != -1:
        name = name.strip(character,"_")
    file = open(f'{name}.csv',mode='w',encoding='utf-8-sig')
    writer =csv.writer(file)
    writer.writerow(['location','info','work_time','pay','reg_date'])
    jobs = brand_info(link)
    for job in jobs:
      writer.writerow(job)
  return

def brand_info(link):
  result = requests.get(link)
  soup = BeautifulSoup(result.text,'html.parser')
  soup = soup.find('div',{'id':'NormalInfo'})
  jobs = []

  location = []
  info = []
  work_time = []
  pay = []
  reg_date = []

  for loca in soup.find_all('td',{'class':'local'}):
    location.append(loca.get_text().replace(u'\xa0', u' '))
  for inf in soup.find_all('span',{'class':'title'}):
    info.append(inf.get_text().replace(u'\xa0', u' '))
  for w_t in soup.find_all('td',{'class':'data'}):
    work_time.append(w_t.get_text())
  for pa in soup.find_all('td',{'class':'pay'}):
    pay.append(pa.get_text())
  for reg in soup.find_all('td',{'class':'regDate'}):
    reg_date.append(reg.get_text())

  for i in range(len(location)):
    jobs.append([location[i],info[i],work_time[i],pay[i],reg_date[i]])
  return jobs