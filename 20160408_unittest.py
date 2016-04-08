import unittest

from unittest_mydict import Dict

class TestDict(unittest.TestCase):

	# 测试值是否与预期相同
	def test_key(self):
		d = Dict()
		d['key'] = 'value'
		self.assertEqual(d.key, 'value')


	# 测试布尔值
	def test_init(self):
		d = Dict(a = 'Michale', b = 'Kobe')
		self.assertTrue(isinstance(d, dict))

	# 测试异常的抛出
	def test_key_error(self):
		d = Dict()
		with self.assertRaises(KeyError):
			value = d['a']

	def test_attr_error(self):
		d = Dict()
		with self.assertRaises(AttributeError):
			value = d.a

	# 执行于每个测试函数之前(比如每个函数都需要提前制造的测试数据)
	def setUp(self):
		print('start test...')

	# 执行于每个测试函数之后(比如清除掉之前提前制造的测试数据)
	def tearDown(self):
		print('test end')

if __name__ == '__main__':
	unittest.main()