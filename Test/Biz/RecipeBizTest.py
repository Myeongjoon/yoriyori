import Biz.RecipeBiz
import Util.ParameterUtil
import unittest

class MessageBizTest(unittest.TestCase):
    # 종료 메시지
    def test_getFoodRecipe(self):
        intent = {'slots' :
        {'targetMonth' :
            {'value' : '8'},
        'material' :
            {'value' : '콩'}}
        }
        self.assertNotEquals(len(Biz.RecipeBiz.getFoodRecipe(intent)),0)

if __name__ == '__main__':
    unittest.main()