# 读取一个文件
try:
	# 打开文件
	f = open('/Users/yangyang/Desktop/1.txt', 'r')
	# 读取文件的全部内容
	print(f.read())
finally:
	if f:
		# 将文件关闭
		f.close()

# 用with语句来自动调用关闭操作
with open('/Users/yangyang/Desktop/1.txt', 'r') as f:
	print(f.read())

# 一行一行地读取文件内容
f = open('/Users/yangyang/Desktop/1.txt', 'r')
for l in f.readlines():
	# 去掉每一行最后的\n
	print(l.strip())

# 每次最多读取x个字节
print(f.read(4))
print(f.read(4))
print(f.read(4))
print(',',f.read(3))

# 所有读取文件产生的对象都是file-like Object

# 读取二进制文件
f = open('/Users/yangyang/Desktop/490FBB9B-60D3-4498-88EF-5D14AEEF51B6.png', 'rb')
print(f.read())

# 指定编码读取文件
f = open('/Users/yangyang/Desktop/1.txt', 'r', encoding= 'gbk')
print(f.read())

# 指定编码读取文件并忽略编码错误
f = open('/Users/yangyang/Desktop/1.txt', 'r', encoding= 'gbk', errors='ignore')
print(f.read())

# 写文件
f = open('/Users/yangyang/Desktop/1.txt', 'w')
f.write('Hello kobe')
f.close()

# with方式省略关闭操作
with open('/Users/yangyang/Desktop/1.txt', 'w') as f:
	print(f.write('Hello Michael'))

# 用字节的方式写入
with open('/Users/yangyang/Desktop/1.txt', 'wb') as f:
	print(f.write(b'ABC'))

# 指定编码写入文件
with open('/Users/yangyang/Desktop/1.txt', 'w', encoding = 'utf-8') as f:
	print(f.write('Hello Michael'))


