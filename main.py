import json
import Biz.MessageBiz
import Biz.RecipeBiz

#요리짱 응답 생성
def CreateResponse(request,value):
    values = {"value" : value,"lang" : "ko","type" : "PlainText"}
    outputSpeech = {"values" : values,"type": "SimpleSpeech"}
    response = {"outputSpeech" : outputSpeech, "card": {},"directives": [],"shouldEndSession": False}
    req = request['request']
    intent = req['intent']
    slots = intent['slots']
    if intent['name'] == '이달의식재료' :
        sessionAttributes = {'intent' : intent['name'],'targetMonth' : slots['targetMonth']['value']}
    else :
        sessionAttributes = req['sessionAttributes']
    res = {"version": "0.1.0","sessionAttributes": sessionAttributes,"response" : response}
    return json.dumps(res)

#요리짱 코어
def yoriJJangCore(request):
    req = request['request']
    type = req['type']
    if type =='LaunchRequest' :
        return Biz.MessageBiz.HelloIntent()
    intent = req['intent']
    name = intent['name']
    if name == 'Clova.GuideIntent' :
        return Biz.MessageBiz.HelloIntent()
    elif name == '이달의레시피' :
        return Biz.MessageBiz.getFoodRecipe(request)
    elif name == '이달의식재료' :
        return Biz.MessageBiz.getMonthFoodMaterialMessage(intent)
    elif name == '다른요리알려줘' :
        return Biz.MessageBiz.getMonthFoodMaterialMessage(intent)
    elif name =='Clova.ExitExtensionIntent' :
        return Biz.MessageBiz.getExitExtensionIntent()
    else :
        return Biz.MessageBiz.HelloIntent()

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