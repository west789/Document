import unittest

from mydict import Dict, Student, add

# class TestDict(unittest.TestCase):
#     def test_init(self):
#         d = Dict(a=1, b='test')
#         self.assertEqual(d.a, 1)
#         self.assertEqual(d.b, 'test')
#         self.assertTrue(isinstance(d, dict))

#     def test_attr(self):
#         d = Dict()
#         d.key = 'value'
#         self.assertTrue('key' in d)
#         self.assertEqual(d['key'], 'value')
    
#     def test_keyerror(self):
#         d = Dict()
#         with self.assertRaises(KeyError):
#             value = d['empty']

# class TestStudent(unittest.TestCase):
#     def test_init(self):
#         stu = Student("Tom", 30)
#         self.assertEqual(stu.name, "Tom")
#         self.assertEqual(stu.score, 30)

class TestAdd(unittest.TestCase):
    
    def test_add(self):
        result = add(4)
        self.assertTrue(result)
        # self.assertNotEqual(result, 12)
        # add = unittest.mock.Mock(return_value=12)
        # result = add()
        # self.assertEqual(result, 12)

if __name__ == '__main__':
    unittest.main()