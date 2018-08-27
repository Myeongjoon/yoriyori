from bs4 import BeautifulSoup
from getRandomIDataInArray import getRandomIDataInArray
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
    return getRandomIDataInArray(getMonthFoodMaterialListCore(mon),3)

#이달의 요리 재료 기능 - 코어
def getMonthFoodMaterialListCore(mon):
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
#구글 클라우드 라우터
def yoriJJangRouter(request):
    request_json = request
    req = request_json['request']
    intent = req['intent']
    if intent['name'] == '이달의식재료' :
        return getMonthFoodMaterialMessage(intent)


#이달의 요리 재료 기능 - 테스트
if __name__ == "__main__":
    import json

    print(getRandomIDataInArray(getMonthFoodMaterialListCore("01"),3))
    print(getRandomIDataInArray(getMonthFoodMaterialListCore("02"),3))
    from pprint import pprint

    with open('test.json') as f:
        data = json.load(f)
    print(yoriJJangRouter(data))
