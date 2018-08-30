from getRandomIDataInArray import getRandomIDataInArray
from getMonthFoodMaterialMessage import getMonthFoodMaterialListCore
from main import yoriJJangCore
from main import CreateResponse
from pprint import pprint
import json

#이달의 요리 재료 기능 - 테스트
if __name__ == "__main__":
    print(getRandomIDataInArray(getMonthFoodMaterialListCore("01"),3))
    print(getRandomIDataInArray(getMonthFoodMaterialListCore("02"),3))
    
    with open('test.json') as f:
        data = json.load(f)
    print(yoriJJangCore(data))
    print(CreateResponse(yoriJJangCore(data)))
