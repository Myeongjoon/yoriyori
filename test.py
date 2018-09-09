
from main import yoriJJangCore
from main import CreateResponse
from pprint import pprint
import Util.ParameterUtil
import Biz.MessageBiz
import json

#이달의 요리 재료 기능 - 테스트
if __name__ == "__main__":
    print(Util.ParameterUtil.getRandomIDataInArray(Biz.MessageBiz.getMonthFoodMaterialListCore("01"),3))
    print(Util.ParameterUtil.getRandomIDataInArray(Biz.MessageBiz.getMonthFoodMaterialListCore("02"),3))
    
    with open('test.json') as f:
        data = json.load(f)
    print(yoriJJangCore(data))
    print(CreateResponse(yoriJJangCore(data)))
