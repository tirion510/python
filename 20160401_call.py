class Chain(object):

	def __init__(self, path = ''):
		self._path = path

	def __getattr__(self, path):
		return Chain('%s/%s' % (self._path, path))

	def __str__(self):
		return self._path

	__repr__ = __str__

	def __call__(self, arg):
		self._path = '%s/%s' % (self._path, arg)
		return self

print(Chain().com.ins.user.list)


#假如我们想将一些动态参数放入URL中
#实现github/users/:uid
print(Chain().github.users('tirion'))

#实现github/users/:uid/dashboard
print(Chain().github.users('tirion').dashboard)


#今天结束啦   谢谢大家的观看以及竹子

#晚上在家会有语音

#就不用打字了

#Bye