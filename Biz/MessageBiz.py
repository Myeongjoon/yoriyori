from bs4 import BeautifulSoup
from Util import ParameterUtil
import json
import urllib.request
import urllib.parse
from Biz import RecipeBiz

#종료 메시지
def getExitExtensionIntent():
    return "제철 메뉴가 고민일땐 이달의 식재료를 불러주세요. 오늘도 맛깔진 하루 보내시길 바래요!"

#시작시 실행되는 인사말 인텐트:
def HelloIntent():
    return '안녕하세요. 이달의 식재료 입니다. 저는 계절에 맞는 제철 식재료와 요리를 추천해드려요. 알고 싶은 월의 이름을 말해주세요. 예를들어 10월의 식재료를 알고 싶다면 10월! 이라고 말씀해주세요'

#이달의 식재료 리스트 리턴
def getMonthFoodMaterialMessage(request):
    req = request['request']
    intent = req['intent']
    name = intent['name']
    targetMonth = ''
    Material=''
    if name=='이달의식재료':
        targetMonth = intent['slots']['targetMonth']['value']
        Material = RecipeBiz.getMonthFoodMaterialList(intent);
    elif name=='다른요리알려줘':
        targetMonth = request['session']['sessionAttributes']['targetMonth']
        Material = request['session']['sessionAttributes']['material']
    mon = ParameterUtil.ConvertMonthToStr(targetMonth)
    ranPrefix = ['신선한','짱맛난','맛깔난']
    return mon + ' 제철 식재료는 ' + Material + "에요. 이 중 원하시는 식재료를 골라주세요. "+ParameterUtil.getRandomDataFromSql(ranPrefix,1,2)+" 재료를 추천해 드릴게요."


#이달의 식재료 리스트 리턴
def getFoodRecipe(request):
    slots = request['request']['intent']['slots']
    req = request['request']
    intent = req['intent']
    name = intent['name']
    Material=''
    if name=='이달의레시피':
        Material = slots['targetMaterial']['value']
    elif name=='다른요리알려줘':
        Material = request['session']['sessionAttributes']['material']
    targetMonth = request['session']['sessionAttributes']['targetMonth']
    mon = ParameterUtil.ConvertMonthToStr(targetMonth)
    recipe = RecipeBiz.getFoodRecipe(targetMonth,Material)
    return mon+'에 먹는 '+Material+' 요리! '+recipe+'는 어떠세요? 다른 '+Material+' 요리를 알고 싶으시다면 다른요리알려줘 라고 말씀해주세요. 필요 없으시면 필요없어라고 말씀해주세요.'
