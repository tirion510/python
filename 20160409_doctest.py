def abs(n):
	'''
	Function to get abslote value of number.

	Example:

	>>> abs(1)
	1
	>>> abs(-1)
	1
	>>> abs(0)
	0
	'''
	return n if n >= 0 else (-n)

class Dict(dict):
	'''
	>>> d = Dict(a = 1,b = 2)
	>>> d['a']
	1
	>>> d['b']
	2
	'''
	def __init__(self, **kw):
		super(Dict, self).__init__(**kw)

# 在命令行执行本文件时执行文档测试
if __name__ == '__main__':
	# 引入文档测试
	import doctest
	# 执行
	doctest.testmod()


# 当测试代码通过，则不会有任何输出

# 不通过则会打印出错误内容

# 不应当取代测试用例，用作开源代码的帮助文档