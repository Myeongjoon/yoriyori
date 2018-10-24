from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
from Util import ParameterUtil
from Biz import MySqlDac

#이달의 요리 재료 기능
def getFoodRecipe(mon,material):
    mon = ParameterUtil.ConvertMonthParameter(mon)
    print('getFoodRecipe :  mon : ' + mon + ' material : ' + material);
    return ParameterUtil.getRandomData(getFoodRecipeCore(mon,material),1)


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
        print('words : ' + str(words))
    res = [word for word in words if material in word]
    print(res)
    return res


# 이달의 식재료 리스트 리턴
def getMonthFoodMaterialList(intent):
    slots = intent['slots']
    mon = slots['targetMonth']['value']
    mon = ParameterUtil.ConvertMonthParameter(mon)
    materials = MySqlDac.getAllMaterial(mon)
    return ParameterUtil.getRandomData(materials, 5)
