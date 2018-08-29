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

#시작시 실행되는 인사말 인텐트:
def HelloIntent():
    return '안녕하세요. 요리요리 입니다.'
#요리짱 코어
def yoriJJangCore(request):
    req = request['request']
    intent = req['intent']
    name = intent['name']
    if name == 'Clova.GuideIntent' :
        return HelloIntent()
    elif name == '이달의식재료' :
        return getMonthFoodMaterialMessage(intent)

#구글 클라우드 라우터
def yoriJJangRouter(request):
    return yoriJJangCore(request.get_json())

#테스트용 함수
def yoriJJangRouterTester(request):
    return yoriJJangCore(request)

#이달의 요리 재료 기능 - 테스트
if __name__ == "__main__":
    import json

    print(getRandomIDataInArray(getMonthFoodMaterialListCore("01"),3))
    print(getRandomIDataInArray(getMonthFoodMaterialListCore("02"),3))
    from pprint import pprint

    with open('test.json') as f:
        data = json.load(f)
    print(yoriJJangRouterTester(data))
