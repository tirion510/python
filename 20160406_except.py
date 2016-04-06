import logging
#定义一个方法
def foo():
	return -1
# 定义一些错误码来表示异常情形
def do_something():
	r = foo()
	if r == (-1):
		print('Error')
	else:
		pass

#java 异常捕捉
# try{
	
# }catch(Exception ex){
	
# }finally{
	
# }

#python 异常捕捉
try:
	pass
except Error as ex:
	pass
finally:
	pass


# python 捕捉到整除0的异常
try:
	print('start')
	r = 10 / 0
	print('test')
except ZeroDivisionError as er:
	print('except', er)
finally:
	print('finally')
print('end')

# python 没有捕捉到异常
try:
	print('start')
	r = 10 / 2
	print('test')
except ZeroDivisionError as er:
	print('except', er)
finally:
	print('finally')
print('end')


# 捕捉多个异常
try:
	print('start')
	r = 10 / int('agufwi')
	print('test')
except ValueError as er:
	print('ValueError', er)
except ZeroDivisionError as er:
	print('except', er)
finally:
	print('finally')
print('end')

#BaseException是所有异常的父类
try:
	print('start')
	r = 10 / int('agufwi')
	print('test')
except BaseException as ex:
	print('ex', ex)
except ValueError as ex:
	print('ex', ex)
finally:
	print('finally')
print('end')

# BaseException可以作为所有异常的兜底方案
try:
	print('start')
	r = 10 / 0
	print('test')
except ValueError as ex:
	print('ValueError', ex)
except BaseException as ex:
	print('ex', ex)
finally:
	print('finally')
print('end')

# 上层可以捕捉到下层函数的异常
def fun_1(s):
	return 10 / int(s)

def fun_2(s):
	try:
		return fun_1(s) * 2
	except ValueError as ex:
		print('ValueError', ex)
		raise ValueError(ex)

def fun_3():
	try:
		fun_2('rrr')
	except BaseException as ex:
		print('Error', ex)

fun_3()

# 查看异常堆栈信息
def fun_1(s):
	return 10 / int(s)

def fun_2(s):
	return fun_1(s) * 2

def fun_3():
	fun_2('rrr')

fun_3()

# BaseException
def fun_1(s):
	return 10 / int(s)

def fun_2(s):
	return fun_1(s) * 2

def fun_3():
	try:
		fun_2('rrr')
	except BaseException as ex:
		logging.exception(ex)
	finally:
		print('finally')

fun_3()
print('end')

#raise抛出错误
def fun_1():
	raise ValueError('ValueError')

# 自定义异常
class MyError(ValueError):
	pass

def fun_2():
	raise MyError('MyError')

def fun_3():
	fun_2()

fun_3()