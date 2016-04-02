class Fib(object):
	def __init__(self):
		self.a, self.b = 0, 1 # 初始化计数器

	def __iter__(self):
		return self # 迭代本身

	def __next__(self):
	 	self.a, self.b = self.b, self.a + self.b # 计算下一个值
	 	if self.a > 100000: #大于10万时跳出循环
	 		raise StopIteration()
	 	return self.a

	def __getitem__(self, n):
		if isinstance(n, int): #传入的是int
			a, b = 1, 1
			for x in range(n):
				a, b = b ,a + b
			return a
		if isinstance(n, slice): #传入的是切片
			start = n.start #开始
			stop = n.stop #结束
			step = n.step #步长
			if start is None:
				start = 0 #设置默认开始
			if step is None:
				step = 1 #设置默认步长
			a, b = 1, 1
			L = []
			t = -1
			for x in range(stop):
				if x >= start:
					if(t < 0):
						t = 0
					if(t % step == 0):
						L.append(a)
					if(t >= 0):
						t = t + 1
				a, b = b, a + b
			return L

f = Fib()
print(f[:20])
#每隔2个打印一次
print(f[:20:2])