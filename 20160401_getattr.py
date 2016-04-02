class Student(object):
	def __init__(self):
		self.name = 'Michael'

	#通过这种方式，我们将类的属性及方法全部动态化处理了
	def __getattr__(self, attr):
	 	if attr == 'age':
	 		return lambda : 25
	 	elif attr == 'score':
	 		return 64

s = Student()
print(s.name)
print(s.age())
print(s.age)
print(s.score)