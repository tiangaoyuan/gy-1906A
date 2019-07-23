#增
#创建
a = []
#列表最后新增单个值
a.append(1)
a.append("shnjhg")
a.append("90")
print(a)
#合并
b = [3,4,6,8]
#使用+合并两个列表（生成一个新的列表）
print(a+b)
print(a)
#使用extend的方法合并两个列表 （在原来列表的末端添加一个列表的元素）
a.extend(b)
print(a)

#删
#根据下标删除某个元素
a.pop(0)
print(a)
#默认删除列表中最后一位元素
a.pop()
print(a)
#清空一个列表
# a = []
#print(a)
a.clear()
print(a)

#改
#根据下标修改某个元素的值
a[0] = 0
a[1] = 4
#等价
a[0],a[1]=0,4
print(a)

#查
#根据下标查询某个元素
print(a[0])
print(a[1])
# 遍历（借助循环）
for i in a:
    print(i)

#截取
#截取部分数据
print(a[1:3])
#截取倒叙
print(a[::-1])
#隔一个取一个
print(a[::2])
print(len(a))

#成员判断
if(4 in a):
 print("存在列表中")
else:
    print("不存在列表中")
    