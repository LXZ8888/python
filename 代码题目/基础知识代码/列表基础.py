# lst=[] #定义的空列表
# print(type(lst),lst,len(lst))
#
# #定义一个非空列表，包含了整数，浮点数，布尔值，列表[1,2,3]也是lst2中的一个元素，是一个整体
# lst2=[100,"数学成绩",120.5,True,[1,2,3]]
# print(type(lst2),lst2,len(lst2))

# '''列表的拼接'''
# a=[1,2,3]
# b=[4,5,6]
# print(a+b)
#
# '''列表多次打印,'''
# print(a*2)

'''列表的取值和切片'''
#索引    0    1    2      3       4         5
# lst = [100,11.33,True,'hello', 'python',[1,2,3]]
# lst2=['a','b','c']
# print(lst[2]) #单个值获取True
# print(lst[3:5]) #获取多个值 hello python，返回值列表
# print(lst[5][1])  #lst[5]==[1,2,3] ,结果2，嵌套列表值的获取

'''列表倒序输出：1.获取列表多个值（全部的值），切片，2：切片的反序
'''
# a='qingfeng'
# print(a[::-1])
#print(lst[::-1])

'''列表的新增：
append:尾部增加一个值
insert：指定位置增加元素
extend:俩个列表相加'''
# lst.append('qingfeng')
# print(lst)
# lst.insert(4,'学习')
# print(lst)
# newlist=lst.extend(lst2) #没有返回值,在原始列表上新增了一个列表
# print(newlist)
# print(lst)


'''列表的删除
remove是根据值去删除，
pop是根据索引去删除，pop方法是有返回值'''
#lst = [100,11.33,True,'hello', 'python',[1,2,3],True]
#lst.remove(True)
# print(lst)
# a=lst.pop(2) #
# print(a)
# print(lst)

#
# lst.clear() #清空列表
# print(lst)

# del lst[3:5] #删除列表索引为3到索引为4的值
# print(lst)

'''列表的修改'''
    #0        1         2
lua=['java','selenium','postman','java']
# lua[0]='python'
# print(lua)
# #把俩个值替换成一个值：获取这俩个值，赋新的值,加[]
# #['java','自动化测试框架']
# lua[1:3:1]=["自动化测试框架"]
# print(lua)


'''列表的反转:
reverse:改变原始列表
切片[：：:-1]  ：只是获取查询，并不会改变列表原始的值
'''
# print(lua.reverse()) #没有返回值，只是改变了原始的列表
# print(lua)
# print(lua[::-1])
# print(lua)
#print(lua.index('selenium'))
print(lua.count('java'))






