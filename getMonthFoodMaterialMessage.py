from bs4 import BeautifulSoup
from getRandomIDataInArray import getRandomIDataInArray
from datetime import datetime
import json
import urllib.request
import urllib.parse

#이달의 식재료 리스트 리턴
def getMonthFoodMaterialMessage(intent):
    return getMonthFoodMaterialList(intent) + "입니다"

#이달의 식재료 리스트 리턴
def getMonthFoodMaterialList(intent):
    slots = intent['slots']
    mon = slots['targetMonth']['value']
    if(mon == '이달의'):
        mon = str(datetime.today().month)
    if(len(mon)==1):
        mon = "0"+ mon
    return getRandomIDataInArray(getMonthFoodMaterialListCore(mon),3)

#이달의 요리 재료 기능 - 코어
def getMonthFoodMaterialListCore(mon):
    '''
    words = []
    words.append("풋콩")
    words.append("대두")
    words.append("콩")
    words.append("포도")
    return words
    '''
    web_url = "http://koreanfood.rda.go.kr/kfi/foodMonth/list?menuId=PS03599&mon="+mon
    with urllib.request.urlopen(web_url) as response:
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        all_divs = soup.find_all("div",{'class':'foodlist'})
        for i in range(3):
            if i == 0:
                children = all_divs[0].findChildren("dd" , recursive=True)
                words = []
                for child in children:
                    words.append(child.contents[0])
    return words
    
