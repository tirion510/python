class Test(object):
	def test(self, name = 'yuan'):
		print('Test, %s.' % name)

t = Test()
t.test()

print(type(Test))

print(type(t))

# 先定义一个函数
def f(self, name = 'world'):
	print('Hello %s.' % name)

# 使用type()创建类
# 0-类的名称 1-继承的父类的tuple 2-方法名称与函数绑定
Hello = type('Hello', (object,), dict(hello = f))

h = Hello()

h.hello()


# 元类
class ListMetaclass(type):
	def __new__(cls, name, bases, attrs):
		# 添加add方法
		attrs['add'] = lambda self, value : self.append(value)
		return type.__new__(cls, name, bases, attrs)


class MyList(list, metaclass = ListMetaclass):
	pass

l1 = MyList()
l1.add(1)
print(l1)

l2 = list()
l2.add(2) #报错

# 定义字段类
class Field(object):
	def __init__(self, name, column_type):
		self.name = name
		self.column_type = column_type

	def __str__(self):
		return '<%s, %s>' % (self.__class__.__name__, self.name)

# 定义整形字段
class IntegerField(Field):
	def __init__(self, name):
		super(IntegerField, self).__init__(name, 'bigint')

# 定义字符串字段
class StringField(Field):
	def __init__(self, name):
		super(StringField, self).__init__(name, 'varchar(100)')

# 定义映射模板元类
class ModelMetaclass(type):
	def __new__(cls, name, bases, attrs):
		# 排除对名字叫Model的类的修改
		if name == 'Model':
			return type.__new__(cls, name, bases, attrs)
		mappings = dict()
		for k, v in attrs.items():
			if isinstance(v, Field):
				mappings[k] = v
		for k in mappings.keys():
			attrs.pop(k)
		attrs['__mappings__'] = mappings
		attrs['__table__'] = name
		return type.__new__(cls, name, bases, attrs)

# 定义映射模板
class Model(dict, metaclass = ModelMetaclass):
	def __init__(self, **kw):
		super(Model, self).__init__(**kw)

	def __getattr__(self, key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError('object has no attribute %s' % key)

	def __setattr__(self, key, value):
		self[key] = value

	def add(self):
		fields = []
		params = []
		args = []
		for k, v in self.__mappings__.items():
			fields.append(v.name)
			params.append('?')
			args.append(getattr(self, k, None))

		sql = 'insert into %s(%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
		print('SQL:', sql)
		print('ARGS:', str(args))

	def delete_by_id(self):
		sql = 'delete from %s where id = ?' % (self.__table__,)
		print('SQL:', sql)
		print('ARGS:', getattr(self, 'id', None))

# 从Model派生出User
class User(Model):
	id = IntegerField('id')
	name = StringField('name')
	email = StringField('email')
	password = StringField('password')

# 生成User实例
u = User(id = 1, name = 'Kobe', email = 'email.kobe.com', password = 'pwd')

# User实例可调用Model中的方法
u.add()
u.delete_by_id()







