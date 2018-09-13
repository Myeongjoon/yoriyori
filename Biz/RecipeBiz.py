from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import Util.ParameterUtil

#이달의 요리 재료 기능
def getFoodRecipe(request):
    slots = request['request']['intent']['slots']
    mon = request['session']['sessionAttributes']['targetMonth']
    material = slots['material']['value']
    mon = Util.ParameterUtil.ConvertMonthParameter(mon)
    return Util.ParameterUtil.getRandomData(getFoodRecipeCore(mon,material),3)


#이달의 요리 재료 기능 - 코어
def getFoodRecipeCore(mon,material):
    web_url = "http://koreanfood.rda.go.kr/kfi/foodMonth/list?menuId=PS03599&mon="+mon
    with urllib.request.urlopen(web_url) as response:
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        all_divs = soup.find_all("div",{'class':'foodlist'})
        for i in range(3):
            if i == 1:
                children = all_divs[1].findChildren("dd" , recursive=True)
                words = []
                for child in children:
                    words.append(child.contents[0])
    res = [word for word in words if material in word]
    print(res)
    return res


# 이달의 식재료 리스트 리턴
def getMonthFoodMaterialList(intent):
    slots = intent['slots']
    mon = slots['targetMonth']['value']
    mon = Util.ParameterUtil.ConvertMonthParameter(mon)
    return Util.ParameterUtil.getRandomData(getMonthFoodMaterialListCore(mon), 3)


# 이달의 요리 재료 기능 - 코어
def getMonthFoodMaterialListCore(mon):
    web_url = "http://koreanfood.rda.go.kr/kfi/foodMonth/list?menuId=PS03599&mon=" + mon
    print(web_url)
    with urllib.request.urlopen(web_url) as response:
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        all_divs = soup.find_all("div", {'class': 'foodlist'})
        for i in range(3):
            if i == 0:
                children = all_divs[0].findChildren("dd", recursive=True)
                words = []
                for child in children:
                    words.append(child.contents[0])
    print(words)
    return words

