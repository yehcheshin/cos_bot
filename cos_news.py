import requests
from bs4 import BeautifulSoup

#場次活動
def get_cos_news(location="南部"): #location: 北部:n 中部:c 南部：s 全部:''
    if location=='北部':
        location='n'
    elif location=='中部':
        location = 'c'
    elif location=='南部':
        location = 's'
    else :
        location = ''
        
    url = requests.get('https://www.doujin.com.tw/events/alist/all/'+location)
    sp = BeautifulSoup(url.text,"html.parser")
    table = sp.find_all('div',class_='info_con')
    activity_info = table[1].find_all('li')
    info_list = []
    for i,info in enumerate(activity_info):
        info_list.append([text for text in info.stripped_strings])
    print(info_list)
if __name__ =="__main__":
    get_cos_news()