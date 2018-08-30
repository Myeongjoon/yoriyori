from bs4 import BeautifulSoup
from getRandomIDataInArray import getRandomIDataInArray
from MessageBiz import getMonthFoodMaterialMessage
from MessageBiz import getExitExtensionIntent
from datetime import datetime
import json
import urllib.request
import urllib.parse

#시작시 실행되는 인사말 인텐트:
def HelloIntent():
    return '안녕하세요. 요리요리 입니다. 이달의 식재료 추천해줘 라고 말씀해주세요'

#요리짱 응답 생성
def CreateResponse(value):
    values = {"value" : value,"lang" : "ko","type" : "PlainText"}
    outputSpeech = {"values" : values}
    response = {"outputSpeech" : outputSpeech, "type": "SimpleSpeech","card": {},"directives": [],"shouldEndSession": False}
    res = {"version": "0.1.0","response" : response}
    return json.dumps(res)

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
    elif name =='Clova.ExitExtensionIntent' :
        return getExitExtensionIntent()
    else :
        return HelloIntent()

#구글 클라우드 라우터
def yoriJJangRouter(request):
    ret = yoriJJangCore(request.get_json())
    print(ret)
    return CreateResponse(ret)
'''
    {
    "version": "0.1.0",
    "sessionAttributes": {
    "formerIntent": "Clova.GuideIntent",
    "recommendation": 1,
    "recipe": "NaN",
    "step": 0
    },
    "response": {
    "outputSpeech": {
    "type": "SimpleSpeech",
    "values": {
    "type": "PlainText",
    "lang": "ko",
    "value": "안녕하세요. 모두의 요리사 요리왕입니다.\n\r만들고 싶은 음식을 말씀해 주세요.\n\r잘 모르시겠다면 요리왕이 남녀노소 즐길 수 있는 요리를 추천해 드릴께요."
    }
    },
    "card": {},
    "directives": [],
    "shouldEndSession": false
    }
    }'''
