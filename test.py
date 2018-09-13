
from main import yoriJJangCore
from main import CreateResponse
from pprint import pprint
import Util.ParameterUtil
import Biz.MessageBiz
import Biz.RecipeBiz
import json

#이달의 요리 재료 기능 - 테스트
if __name__ == "__main__":
    print(Util.ParameterUtil.getRandomData(Biz.RecipeBiz.getMonthFoodMaterialListCore("01"),3))
    print(Util.ParameterUtil.getRandomData(Biz.RecipeBiz.getMonthFoodMaterialListCore("02"),3))
    request = \
        {'request' :
            {'intent' :
                {'slots' :
                    {'targetMonth' :
                        {'value' : '이달의'},
                    'material' :
                        {'value' : '무화과'}}
                }
            },
          'session' : {
              'sessionAttributes' : {
                  'targetMonth' : '이달의'
              }
          }
        }
    print(Biz.RecipeBiz.getFoodRecipe(request))

    #with open('test.json') as f:
    #    data = json.load(f)
    #print(yoriJJangCore(data))
    #print(CreateResponse(yoriJJangCore(data)))
