from bs4 import BeautifulSoup
from datetime import datetime
import json
import Biz.MessageBiz
import Biz.RecipeBiz
import urllib.request
import urllib.parse


#이미지 테스트
def returnImageView():
    res = {
      "type": "ImageText",
      "imageUrl": {
        "type": "url",
        "value": ""
      },
      "mainText": {
        "type": "string",
        "value": "리오넬 메시"
      },
      "referenceText": {
        "type": "string",
        "value": "검색결과"
      },
      "referenceUrl": {
        "type": "url",
        "value": "https://m.search.contentproviderdomain.com/search?where=m&sm=mob_lic&query=%eb%a6%ac%ec%98%a4%eb%84%ac+%eb%a9%94%ec%8b%9c+%ec%86%8c%ec%86%8d%ed%8c%80"
      },
      "subTextList": [
        {
          "type": "string",
          "value": "FC 바르셀로나"
        }
      ],
      "thumbImageType": {
        "type": "string",
        "value": "인물"
      },
      "thumbImageUrl": {
        "type": "url",
        "value": "http://sstatic.contentproviderdomain.net/people/3/201607071816066361.jpg"
      }
    }
    return res



#요리짱 응답 생성
def CreateResponse(request,value):
    values = {"value" : value,"lang" : "ko","type" : "PlainText"}
    outputSpeech = {"values" : values,"type": "SimpleSpeech"}
    response = {"outputSpeech" : outputSpeech, "card": {},"directives": [],"shouldEndSession": False}
    req = request['request']
    intent = req['intent']
    slots = intent['slots']
    if intent['name'] == '이달의식재료' :
        sessionAttributes = {'intent' : '이달의식재료','targetMonth' : slots['targetMonth']['value']}
    else :
        sessionAttributes = {}
    res = {"version": "0.1.0","sessionAttributes": sessionAttributes,"response" : response}
    return json.dumps(res)

#요리짱 코어
def yoriJJangCore(request):
    req = request['request']
    type = req['type']
    if type =='LaunchRequest' :
        return MessageBiz.HelloIntent()
    intent = req['intent']
    name = intent['name']
    if name == 'Clova.GuideIntent' :
        return MessageBiz.HelloIntent()
    elif name == '이달의레시피' :
        return RecipeBiz.getFoodRecipe(intent)
    elif name == '이달의식재료' :
        return MessageBiz.getMonthFoodMaterialMessage(intent)
    elif name == '이미지' :
        return returnImageView()
    elif name =='Clova.ExitExtensionIntent' :
        return MessageBiz.getExitExtensionIntent()
    else :
        return MessageBiz.HelloIntent()

#구글 클라우드 라우터
def yoriJJangRouter(request):
    print('------- REQUEST ---------')
    print(request.get_json())
    print('------- REQUEST ---------')
    ret = yoriJJangCore(request.get_json())
    print('------- MESSAGE ---------')
    print(ret)
    print('------- MESSAGE ---------')
    res = CreateResponse(request.get_json(),ret)
    print('------- RESPONSE ---------')
    print(res)
    print('------- RESPONSE ---------')
    return res