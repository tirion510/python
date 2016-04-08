import pdb

s = '1'
n = int(s)
pdb.set_trace() # 程序执行到这一行会自动暂停
print(10 / n)

x = 10 / n
pdb.set_trace()
print(x)

# c 用于继续执行代码