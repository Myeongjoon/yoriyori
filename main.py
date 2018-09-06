from bs4 import BeautifulSoup
from getRandomIDataInArray import getRandomIDataInArray

from datetime import datetime
import json
import MessageBiz
import RecipeBiz
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
    mon = slots['targetMonth']['value']
    if(len(mon)==1):
        mon = "0"+ mon
    sessionAttributes = {'mon' : mon}
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
    ret = yoriJJangCore(request.get_json())
    print(ret)
    return CreateResponse(request.get_json(),ret)
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
