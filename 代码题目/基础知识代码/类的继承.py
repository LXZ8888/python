'''
类：代码的复用性，可读性，可靠性
'''

'''单继承'''

# class Person():
#     '''父类，基类'''
#     NAME='人类'
#     __Year='1800'
#
#     def __init__(self,test):
#         print(test)
#         print('我是人类')
#
#     def sleep(self):
#         print('父类的方法：睡觉')
#
# class Stduent(Person):
#     '''子类，派生类'''
#     school='清华'
#
#     def __init__(self,test):
#         Person.__init__(self,test)
#         #super(Stduent,self).__init__(test)
#         print('我是学生类')
#
#     def shangxue(self):
#         print(self.NAME)
#         self.sleep()
#         print('上学')
#
#     def sleep(self):
#         Person.sleep(self)
#         print('子类的方法：睡觉')
#
# class Arts(Stduent):
#     name='艺术生'


# zs=Stduent('11')
# zs.sleep()
# print(zs.NAME)
# zs.sleep()
#zs.shangxue()

# zs=Arts('test')
# print(zs.NAME)


'''
Ø情况一：父类有构造方法，子类没有时，在实例化子类对象时会自动调用父类的构造方法， 即子类自动继承父类的构造方法。
情况二：父类有构造方法，子类有构造方法
    重写
    扩写
'''


'''多继承'''
class ShenXian():
    def fly(self):
        print('飞')


class Monkey():
    def eat(self):
        print('吃')

class SunWUkong(ShenXian,Monkey):
    def bianshen(self):
        print('变身')

swk=SunWUkong()
swk.eat()
swk.fly()
swk.bianshen()
