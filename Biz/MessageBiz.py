from bs4 import BeautifulSoup
from datetime import datetime
import Util.ParameterUtil
import json
import urllib.request
import urllib.parse
import Biz.RecipeBiz

#종료 메시지
def getExitExtensionIntent():
    return "만나서 반가웠어요. 다음에도 요리요리를 불러주세요"

#시작시 실행되는 인사말 인텐트:
def HelloIntent():
    return '안녕하세요. 요리요리 입니다. 이달의 식재료 추천해줘 라고 말씀해주세요'

#이달의 식재료 리스트 리턴
def getMonthFoodMaterialMessage(intent):
    return Biz.RecipeBiz.getMonthFoodMaterialList(intent) + "입니다"


#이달의 식재료 리스트 리턴
def getFoodRecipe(intent):
    return Biz.RecipeBiz.getFoodRecipe(intent) + "입니다"