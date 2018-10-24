from Biz import MySqlDac
import unittest

class MySqlDacTest(unittest.TestCase):
    def test_getAllMaterial(self):
        response = MySqlDac.getAllMaterial(1);
        for tuple in response:
            print(tuple[0])
            print(tuple[1])
            print(tuple[2])

if __name__ == '__main__':
    unittest.main()