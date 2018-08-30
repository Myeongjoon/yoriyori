from bs4 import BeautifulSoup
from getRandomIDataInArray import getRandomIDataInArray
from getMonthFoodMaterialMessage import getMonthFoodMaterialMessage
from datetime import datetime
import flask
import json
import urllib.request
import urllib.parse

#시작시 실행되는 인사말 인텐트:
def HelloIntent():
    return '안녕하세요. 요리요리 입니다. 이달의 식재료 추천해줘 라고 말씀해주세요'

#요리짱 응답 생성
def CreateResponse(value):
    outputSpeech = {"values" : value,"lang" : "ko","type" : "PlainText"}
    response = {"outputSpeech" : outputSpeech}
    res = {"response" : response}
    return json.dumps(response)

#요리짱 코어
def yoriJJangCore(request):
    req = request['request']
    type = req['type']
    if type =='LaunchRequest' :
        return HelloIntent()
    intent = req['intent']
    name = intent['name']
    if name == 'Clova.GuideIntent' :
        return HelloIntent()
    elif name == '이달의식재료' :
        return getMonthFoodMaterialMessage(intent)
    else :
        return HelloIntent()

#구글 클라우드 라우터
def yoriJJangRouter(request):
    return CreateResponse(yoriJJangCore(request.get_json()))
