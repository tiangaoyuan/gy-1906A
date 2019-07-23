#字典的特征


#增
#创建
#增
#创建
a = {}
#字典中新增一对数据
a["姓名"] ="田高远"
print(a)
#改
a["姓名"] ="小田同学"
print(a)

#删
a.pop(1)
del a["姓名"]
print(a)

#改
a["姓名"] = "小田同学"
print(a)

#查
#根据key 查看value

#遍历字典
for key in a:
    print(a[key])

#字典合并
c = {"姓名":"小田","班级":"国宝班"}
d = {"性别":"男"}
c.update(d)
print(c)
#两个字典合并，生成一个新字典
print(dict(c,**d))
print(c)
print(d)
#成员判断（key)
if("性别" in c):
    print()




