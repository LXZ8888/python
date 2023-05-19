'''
练习一：
1：从控制台接受你输入的用户名和密码的值，并输出xxx用户欢迎登陆 （xxx就是你输入的用户名的值）
name=input('请输入用户名：')
password=input('请输入密码：')
print('{}用户欢迎登陆'.format(name))


2：从控制台接受你输入的数字1和数字2的值，并对两个数字进行求和，输出两者的和
'''
a = int(input('输入数字1：'))
b = int(input('输入数字2：'))
print(a + b)

'''
练习二：
1：计算整型50乘以10再除以5的商并使用print输出。（乘法用*，除法用/）
print(int(50*10/5))

2：判断整型8是否大于10的结果并使用print输出。
print(int(8)>10)

3：计算整型30除以2得到的余数并使用print输出。  取余数用(%)符号
print(30%2)

4：使用字符串乘法实现 把字符串”我爱我的祖国”创建三遍并拼接起来最终使用print输出。
'''
print(str('我爱我的祖国' * 3))

练习三：
有变量name = "aleX leNb "完成如下操作：移除name变量对应的值两边的空格, 并输出处理结果
print(name.strip(''))

判断name变量是否以 “al” 开头, 并输出结果（用切片）

print(name[0:2:1] == 'al')

判断name变量是否以”Nb”结尾, 并输出结果（用切片）
print(name[-2:] == 'Nb')

将name变量对应的值中的所有的”l” 替换为 “p”, 并输出结果
print(name.replace('l', 'p'))

将name变量对应的值中的第一个”l”替换成”p”, 并输出结果
print(name.replace('l', 'p', 1))

将name变量对应的值根据所有的”l” 分割, 并输出结果
print(name.split('l'))

将name变量对应的值根据第一个”l”分割, 并输出结果
print(name.split('l', 1))

将name变量对应的值变大写, 并输出结果

print(name.upper())

将name变量对应的值变小写, 并输出结果

print(name.lower())

请输出name变量对应的值的第2个字符?
print(name[1])

请输出name变量对应的值的前3个字符?
print(name[:3])

请输出name变量对应的值的后2个字符?
print(name[-2:])

练习四：
有字符串s = "123a4b5c"通过对s切片形成新的字符串"123"
S1 = s[:3]
print(s1)

通过对s切片形成新的字符串"a4b"
S2 = s[3:6]
print(s2)

通过对s切片形成字符串s5, s5 = "c"
s5 = [-2]
print(s5)

通过对s切片形成字符串s6, s6 = "2abc"
'''
s6 = s[-3::-2]
print(s6)






'''
练习五：列表
'''

# 一、列表练习题：
# 1：写代码，有如下列表，按照要求实现每一个功能。
#li = ['alex', 'WuSir', 'ritian', 'barry', 'wenzhou']
# 计算列表的长度并输出
print(len(li))
# 请通过步长获取索引为偶数的所有值，并打印出获取后的列表

print(li[::2])

# 列表中追加元素”seven”,并输出添加后的列表
li.append("seven")

# 请在列表的第1个位置插入元素”Tony”,并输出添加后的列表
li.insert(0,"Tony")
print(li)


# 请修改列表第2个位置的元素为”Kelly”,并输出修改后的列表
li[1] = "Kelly"
 print(li)


# 请将列表的第3个位置的值改成 “太白”，并输出修改后的列表
li[2]='太白' 
print(li)


#请将列表 l2=[1,”a”,3,4,”heart”] 的每一个元素追加到列表li中，并输出添加后的列表
l2=[1,"a",3,4,"heart"] 
for i in range(len(l2)): 
li.append(l2[i]) 
print(li)

# 请将字符s = “qwert”的每一个元素添加到列表li中，要求一行代码实现不允许循环添加。
s = "qwert" 
li.extend(','.join(s).split(',')) 
print(li)

# # 请删除列表中的元素”ritian”,并输出删除元素后的列表
li.remove('ritian') 
print(li)

# 请删除列表中的第2个元素，并输出删除元素后的列表
 print(li.pop(1))


# 请删除列表中的第2至第4个元素，并输出删除元素后的列表
del li[1:4]
 print(li)

# 2：写代码，有如下列表，利用切片实现每一个功能
#li = [1, 3, 2, 'a', 4, 'b', 5,'c']
#通过对li列表的切片形成新的列表 [1,3,2]
print(li[:3])

# 通过对li列表的切片形成新的列表 [“a”,4,”b”]
print(li[3:6])

# 通过对li列表的切片形成新的列表 [1,2,4,5]
print(li[::2])

# 通过对li列表的切片形成新的列表 [3,”a”,”b”]
print(li[1:-1:2])

# 通过对li列表的切片形成新的列表 [3,”a”,”b”,”c”]
print(li[1::2])


# 通过对li列表的切片形成新的列表 [“c”]
print(li[-1:])


# 通过对li列表的切片形成新的列表 [“b”,”a”,3] 反序 取列表索引为奇数
print(li[-3::-2])



 3：写代码，有如下列表，按照要求实现每一个功能。
lis = [2, 3, 'k', ['qwe', 20, ['k1', ['tt', 3, '1']], 89], 'ab', 'adv']
# # 将列表lis中的”k”变成大写，并打印列表。
lis[2]='K' 
lis[3][2][0]='K' 
print(lis)

# 将列表中的数字3变成字符串”100”

lis[3][2][1][1] = "100"
lis[1] = "100"
print(lis)

# 将列表中的字符串”tt”变成数字 101
lis[3][2][1][0] = 101 
print(lis)


# 在 “qwe”前面插入字符串：”火车头”
lis[3].insert(0,'火车头') 
print(lis)


'''
# 练习七：字典
'''
# 1：根据需求写代码
dic = {'k1': 'v1', 'k2': 'v2', 'k3': [11,22,33]}
#请在字典中添加一个键值对，"k4": "v4"，输出添加后的字典
dic["k4"]="v4" 
print(dic)


# 请在修改字典中 "k1" 对应的值为 "alex"，输出修改后的字典
dic["k1"]="alex" 
print(dic)

# 请在k3对应的值中追加一个元素 44，输出修改后的字典

dic['k3'].append(44)
print(dic)

# 请在k3对应的值的第 1 个位置插入个元素 18，输出修改后的字典
dic['k3'].insert(0,18)
print(dic)




2：根据需求写代码
dic1 = {
    'name':['alex',2,3,5],
    'job':'teacher',
    'oldboy':{'alex':['python1','python2',100]}
}
# 1，将name对应的列表追加一个元素’wusir’。

dic1["name"].append("wusir") 
print(dic1)

# 2，将name对应的列表中的alex首字母大写。 capitalize首字母大写

dic1["name"][0]=dic1["name"][0].capitalize()
print(dic1)

# 3，oldboy对应的字典加一个键值对’老男孩’,’linux’。
dic1["oldboy"]['老男孩']='linux' 
print(dic1)


# 4，将oldboy对应的字典中的alex对应的列表中的python2删除

dic1["oldboy"]['alex'].pop(1) 
print(dic1)
