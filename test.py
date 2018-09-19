
from main import yoriJJangCore
from main import CreateResponse
from pprint import pprint
import Util.ParameterUtil
import Biz.MessageBiz
import Biz.RecipeBiz
import json

print(Util.ParameterUtil.getRandomData(['1','2','3','4'],3))
print(Util.ParameterUtil.getRandomData(['1','2','3','4'],3))
print(Util.ParameterUtil.getRandomData(['1','2','3','4'],3))
print(Util.ParameterUtil.getRandomData(['1','2','3','4'],3))
print(Util.ParameterUtil.getRandomData(['1','2','3','4'],3))
#이달의 요리 재료 기능 - 테스트
if __name__ == "__main__":
    print(' --- unit test --- ')
    print(Util.ParameterUtil.getRandomData(Biz.RecipeBiz.getMonthFoodMaterialListCore("01"),3))
    print(' --- unit test --- ')
    slots = {'slots':
         {'targetMonth':
              {'value': '이달의'},
          'material':
              {'value': '무화과'}}
     }
    print(Biz.MessageBiz.getMonthFoodMaterialMessage(slots))
    print(' --- unit test --- ')
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

    print(' --- unit test --- ')
    print(Biz.MessageBiz.getFoodRecipe(request))
    print(' --- unit test --- ')
