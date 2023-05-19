'''匿名函数'''

# def fun1(m):
#     '''求平方的函数'''
#     return m**2
#
# def fun2(a,b):
#     '''求和的方法'''
#     return a+b
# print(fun1(10))
# res=lambda m:m**2
# print(res(10))
# print(fun2(1,6))
# res1=lambda a,b:a+b
# print(res1(2,3))

# l=[10,20,30]
# res1=lambda l:sum(l)
# print(res1(l))
#
# res2=lambda l:max(l)
# print(res2(l))
#
# res=lambda *agrs:sum(agrs)
# print(res(1,3,5,7,8))
import logging

'''装饰器：
获取方法名称: 方法名称.__name__
需求：每个函数执行的时候打印日志，函数的运行时间
'''
import time
# def loging_fun(fun):
#     '''封装一个打印函数执行的方法:执行方法之前先打印日志，再执行这个方法'''
#     #logging.warning('{}函数开始执行'.format(fun.__name__))
#     start_time=time.time() #获取函数执行之前的时间
#     fun()
#     end_time=time.time() #获取函数执行之后的时间
#     run_time=end_time-start_time
#     logging.warning('执行了{0}函数,执行时间{1:.2}'.format(fun.__name__,run_time))

'''装饰器:是一个返回值是函数的 函数'''
def log(func): #func=fun1
    '''log方法的返回值就是原始函数的返回值'''
    def wrapper(*args,**kwargs):
        '''wrapper方法的返回值就是原始函数的返回值'''
        start_time=time.time() #获取函数执行之前的时间
        res=func(*args,**kwargs)          #执行原始函数的过程 fun1()
        end_time=time.time() #获取函数执行之后的时间
        run_time=end_time-start_time #运行时间
        logging.warning('执行了{0}函数,执行时间{1:.2}'.format(func.__name__,run_time))
        return res #返回原始函数的返回值
    return wrapper      #装饰器固定语法，返回一个函数

'''装饰器运行过程
1.调用函数，先执行@log：相当于执行了语句 fun1=log(fun1) 
2.fun1() =wrapper()，调用方式不变，实际是执行了装饰器里面的wrapper
'''

@log
def fun1():
    #time.sleep(2)  #等待2秒钟
    print('函数1')
    return '这是fun1'
    #logging.warning('{}函数开始执行'.format(fun1.__name__))

@log
def fun2():
    print('函数2')
    return '这是fun2'
    #time.sleep(3)  #等待3秒钟
    #logging.warning('{}函数开始执行'.format(fun2.__name__))
    # return name



# loging_fun(fun1)
# loging_fun(fun2)

res1=fun1()
print(fun1.__name__)  #wrapper
res2=fun2()
print(fun2.__name__)
print(res1,res2)
# print(fun1)
#fun1()
# res=fun2(fun1)
# print(res)








