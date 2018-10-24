import json
from Biz import MessageBiz

#요리짱 응답 생성
def CreateResponse(request,value):
    values = {"value" : value,"lang" : "ko","type" : "PlainText"}
    outputSpeech = {"values" : values,"type": "SimpleSpeech"}
    response = {"outputSpeech" : outputSpeech, "card": {},"directives": [],"shouldEndSession": False}
    req = request['request']
    intent = req['intent']
    slots = intent['slots']
    if intent['name'] == '이달의식재료' :
        sessionAttributes = {'targetMonth' : slots['targetMonth']['value']}
    elif intent['name']  == '이달의레시피' :
        tempSessionAttributes = request['session']['sessionAttributes']
        tempSessionAttributes['material'] = slots['material']['value']
        sessionAttributes = request['session']['sessionAttributes']
    else :
        sessionAttributes = request['session']['sessionAttributes']
    sessionAttributes['intent'] = intent['name']
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
        return MessageBiz.getFoodRecipe(request)
    elif name == '이달의식재료' :
        return MessageBiz.getMonthFoodMaterialMessage(request)
    elif name == '다른요리알려줘' :
        return MessageBiz.getFoodRecipe(request)
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