# tp1=() #定义一个空元祖
# print(id(tp1),tp1,type(tp1))
#定义一个非空元祖，包含了一个元素,需要在元素后加上逗号
# tp2=("test",)
# # print(id(tp2),tp2,type(tp2))
# #定义一个非空元祖，包含了多个个元素,需要在元素后加上逗号
# tp3=("test",
#      1,
#      3.14,
#      True,
#      [1,2,3],
#      ('a','b','c')
#      )
# print(id(tp3),tp3,type(tp3))
# print(tp2+tp3)
# print(tp2*8)

# print(tp3[3])
# print(tp3[3:6])
# print(tp3[::-1])
# print(tp3[4][1]) #2
# print(tp3[5][1]) #b


'''元祖不可变，元祖的列表可以改变吗'''
# l1=[1,2,3]
# l1[0]=4
# l1[1]=5
# l1[2]=6
# print(l1)
# tp3[4][0]=4  #tp3[4]就是一个列表
# tp3[4][1]=5
# tp3[4][2]=6
# print(tp3)


'''内存空间'''
# l1=[1,2,3,4,5,6]
# tp1=(1,2,3,4,5,6)
# print(l1.__sizeof__())
# print(tp1.__sizeof__())


# def test():
#     name='qingfeng'
#     city='长沙'
#     return name,city
# print(test())

'''
字典
'''
#空字典
# d1={}
# print(id(d1),d1,type(d1))
#非空字典
# d2={
#     "name":"qingfeng",  #name（key）,qingfeng(value),
#     "电话":"150909888789",
#     "h":"178",
# }
# # print(id(d2),d2,type(d2))
# # print(len(d2))
#
# print(d2['name']) #查字典的value

# d3={
#     'id':1001,'name':'lisa','age':18,
#     'skill':['python','自动化测试','性能测试 ','接口测试 '],
#     'hobby':('singing','swimming'),
#     'addr':{'company':'北京','local':'长沙 '}
#     }
# print(d3['skill'][1]) #自动化测试
# print(d3['hobby'][1]) #swimming
# print(d3['addr']['local']) #长沙
#
# #字典新增值：phone:112323
# d3['phone']='18937483594'
# print(d3)
#
# #新增值的时候，key存在了，就会替换值
# d3['id']=10086
# print(d3)


#pop()方法,有返回值的，删除字典值,会返回你删除的值
# id=d3.pop('id')
# print(id)
# print(d3)

#popitem()方法：有返回值的,删除并返回字典中的最后一对键和值
# addr=d3.popitem()
# print(addr)
# print(d3)

# d3.clear() #没有返回值的
# print(d3)

# del d3['id'] #没有返回值的
# print(d3)

'''
字典常用其他方法：
字典名.items()：返回可遍历的（键，值）元组数组
字典名.keys()：返回一个字典所有的键，返回一个迭代器，可以使用 list()  来转换为列表
字典名.values()：返回一个字典所有的值，返回一个迭代器，可以使用 list()  来转换为列表
字典名.get(key,default)：根据key去字典中获取对应的值，如果key不存在则 返回None
'''
d3={
    'id':1001,
    'name':'lisa',
    'age':18,
    'skill':['python','自动化测试','性能测试 ','接口测试 '],
    'hobby':('singing','swimming'),
    'addr':{'company':'北京','local':'长沙 '}
    }
print(d3.items()) #每一组
print(list(d3.keys())) #每一组中的key
print(list(d3.values())) #每一组中的value
print(d3['id'])
print(d3.get('id'))