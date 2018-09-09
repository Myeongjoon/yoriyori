import Biz.MessageBiz
import unittest

class MessageBizTest(unittest.TestCase):
    # 종료 메시지
    def test_getExitExtensionIntent(self):
        self.assertEqual(Biz.MessageBiz.getExitExtensionIntent(),"만나서 반가웠어요. 다음에도 요리요리를 불러주세요")

    # 시작시 실행되는 인사말 인텐트:
    def test_HelloIntentTest(self):
        self.assertEqual(Biz.MessageBiz.HelloIntent(),'안녕하세요. 요리요리 입니다. 이달의 식재료 추천해줘 라고 말씀해주세요')

if __name__ == '__main__':
    unittest.main()