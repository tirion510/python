def fun_1(s):
	n = int(s)
	assert n != 0, 'n can not be zero!'
	return 10 / n

def fun_2():
	fun_1('0')

fun_2()

# 遗留问题
# python3 -0 屏蔽断言使用方式