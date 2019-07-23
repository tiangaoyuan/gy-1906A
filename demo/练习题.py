# 如何取一个url  协议名 域名 uri
a="http://qa.yansl.com/admin/logs"
xieyi=a.split("://")[0]
a=a.split("://")[1]

print(xieyi)
print(a)

yuming=a[:a.find("/")]
print(yuming)

uri = a[a.find("/"):]
print(uri)