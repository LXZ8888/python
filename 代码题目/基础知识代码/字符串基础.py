# age=18
# height=170
# print(age+height)
# phone=12355457784
# print(age,height,phone)
# print(type(age))
#
# '''python定一个对象，基本的三要素：值,类型，id(整数，唯一标识符)'''
# print(id(age),id(phone),id(height))
#
# price=3.8
# print(price,type(price),id(price))


'''字符串'''
#a='' #空的字符串
# print(a,type(a),id(a))
# print('a的长度：',len(a))
#
# b='changsha长沙'  #非空字符串
# print(b)

'''\转义字符 \n表示换行'''
# name="i\"m,qing\'feng\n"
# xueli='ben\'ke\n'
# city='''长沙'''
# card='4305222455'
# print(city*3)

'''r表示不转义'''
# dir='D:\qingfengtest\node'
# dir1=r'D:\qingfengtest\node'
# print(dir)
# print(dir1)

'''字符串根据索引取值'''
# l='python'
# print(l[3]) # 正序：获取字符串第四个值
# print(l[-3]) #反序：获取从右往左第三个值
# print(l[5])  #获取字符串最后一个字符的值，获取这个字符串的长度print(l[len(l)-1])

'''切片'''
#l='learnpythonhappy'  #正序6-11 python
# print(l[5:11])
# print(l[5:11:1])
# print(l[5:11:2])

#print(l[-11:-5:1]) #反序-11--6获取python

#从右到左,部长为负数
#print(l[-6:-12:-1])  #nohtyp  -6-11

'''布尔值：bool方法'''
#
# n=10  #True
# a=0   #False
# s=''  #False
# m='jklj'  #True
#
# print(bool(n),bool(a),bool(s),bool(m))

'''多个条件判断：与算法and 俩个同时为真才为真，否则为假
               或运输or,只要有一个为真，结果就为真
               非运算 not
'''
# print(True and True)
# print(bool(n) and bool(m))
# print(True and False)
# print(False or True)
# print(True or False)
# print(False or False)
# print(not True)
# print(not False)


'''字符串常用方法'''
#l='learnpythonhappy'
#s='4302565655454x'
# print(l.startswith('x'))
# print(l.endswith('y'))
# '''判断字符串是否以l开头，以y结尾'''
# print(l.startswith('l') and l.endswith('y'))
#print(s.isdigit()) #判断一个身份证号码是否包含了字母x

#m='  fd   sio   jh  jh   '
# print(m)
# #print(m.strip('f'))
# # print(m.lstrip()) #去掉左边
# print(m.rstrip()) #去掉右边空格

# x='###jkljfdsf%%%##'
# print(x.replace('#','%',1)) #替换次数不填，默认替换所有的
# print(m.replace(' ',''))

# print(l.upper())
# print(l.lower())


msg='qingfeng&changsha&18'
print(msg.split('&'))
print(msg.split('&',1))#分离次数不填，默认分离所有的
