import unittest
import myunit
# 自己的测试类必须继承unittest.TestCase
# class MyTest(unittest.TestCase):
#     def setUp(self):
#         print("测试开始前自动执行")
#     def tearDown(self):
#         print("测试结束")
#     def test_add(self):
#         self.assertEqual(myunit.add(3,4),8,'加法错误')
# if __name__ == "__main__":
#     unittest.main()

class TestDog(unittest.TestCase):
    def test__init(self):
        dog = myunit.Dog('tom',5)
        self.assertEqual(dog.name,'tom1','init：姓名错误')

if __name__ == "__main__":
    unittest.main()










