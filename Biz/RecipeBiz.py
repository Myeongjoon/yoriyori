from bs4 import BeautifulSoup
from datetime import datetime
import json
import urllib.request
import urllib.parse
import Util.ParameterUtil

#이달의 요리 재료 기능
def getFoodRecipe(intent):
    slots = intent['slots']
    mon = slots['targetMonth']['value']
    material = slots['material']['value']
    mon = Util.ParameterUtil.ConvertMonthParameter(mon)
    return getFoodRecipeCore(mon,material)


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
    return [ word for word in words if material in word]
