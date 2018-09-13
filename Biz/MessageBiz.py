from bs4 import BeautifulSoup
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
    Material = Biz.RecipeBiz.getMonthFoodMaterialList(intent);
    targetMonth = intent['slots']['targetMonth']
    mon = Util.ParameterUtil.ConvertMonthToStr(targetMonth)
    ranPrefix = ['신선한','짱맛난','맛깔난']
    return mon + ' 제철 식재료는 ' + Material + "에요. 이 중 원하시는 식재료를 골라주세요. "+Util.ParameterUtil.getRandomData(ranPrefix,1)+" 재료를 추천해 드릴게요."


#이달의 식재료 리스트 리턴
def getFoodRecipe(request):
    slots = request['request']['intent']['slots']
    mon = request['session']['sessionAttributes']['targetMonth']
    material = slots['material']['value']
    mon = Util.ParameterUtil.ConvertMonthToStr(mon)
    recipe = Biz.RecipeBiz.getFoodRecipe(request)
    return mon+'에 먹는 '+material+' 요리! '+recipe+'는 어떠세요? '+recipe+' 레시피를 원하시면 레시피 보내줘 라고 말씀해주세요. 필요 없으시면 필요없어라고 말씀해주세요.'
