'''
练习一：每次跑步会减肥0.5 公斤，每次吃东西体重会增加1公斤，把多个对象共同的功能封装为实例方法
练习二：写一个员工类，统计员工的总人数，展示员工的基本信息，根据员工的工作年限评判员工等级
1.定义一个类变量,统计员工的人数
2.展示员工的基本信息
3.增加类的方法；评判员工等级
'''


# class Person():
#     def __init__(self,name,weight):
#         self.name=name
#         self.weight=weight
#
#     def run(self):
#         self.weight-=0.5
#         print('姓名为：{0}爱运动，体重为{1}'.format(self.name,self.weight))
#
#     def eat(self):
#         self.weight+=1
#         print('姓名为：{0}是个吃货，体重为{1}'.format(self.name,self.weight))
#
# # xiaoming=Person()
# # xiaoming.name='小明'
# # xiaoming.weight='60'
# xiaoming=Person('小明',60)
# zhangsan=Person('张三,',90)
# # print(xiaoming.weight,zhangsan.weight)
# xiaoming.eat()
# zhangsan.run()
# print(xiaoming.weight,zhangsan.weight)

# class Emp():
#     '''员工类'''
#     empCount=0 #员工人数初始值，默认为0 empCount+1=
#     __money='100'
#     def __init__(self,name,age,years,money):
#         self.name=name
#         self.age=age
#         self.years=years
#         self.__money=money
#         Emp.empCount+=1
#
#     def display_info(self):
#         print('员工编号{}：姓名：{}，年龄：{}，工作年限：{},余额{}'.format(
#                 Emp.empCount,self.name,self.age,self.years,self.__money
#         ))
#         #self.__test()
#     def emp_rank(self):
#         '''评定员工等级'''
#         if self.years>=10:
#             print('P1')
#         elif self.years>5:
#             print('P2')
#         elif self.years>2:
#             print('P3')
#         else:
#             print('P4')
#
#     @property
#     def money(self):
#         return  self.__money
#
#
#     # def __test(self):
#     #     print('我是私有方法')
# A=Emp('zhangsan',26,4,1688)
# # A.display_info()
# print(A.money)




# A.emp_rank()
# B=Emp('lisi',35,10)
# B.display_info()
# B.emp_rank()

# print('类的属性和方法',Emp.__dict__)
# print('实例的属性',A.__dict__)
# print(Emp.__name__)


class CLanguage:
    # 类构造方法，也属于实例方法
    def __init__(self):
        self.name = "清风"

    # 下面定义了一个类方法
    @classmethod
    def info(cls):
        print("正在调用类方法", cls)

    #定义了一个类静态方法
    @staticmethod
    def test():
        print('1111')



print(CLanguage)

print(CLanguage.info())

