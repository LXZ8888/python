from flask import Flask,render_template,jsonify
from flask import request
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

'''用户相关的接口
用例相关的接口
商品相关的接口
分模块
'''

'''测试开发重点在测试
重点在自动化的落实，把这些自动化展现的方式到页面，而不是代码和工具
'''
# 传入__name__初始化一个Flask实例
# app.route装饰器映射URL和执行的函数。这个设置将根URL映射到了hello_world函数上
#视图函数名称一定不能重复
# 运行本项目，host=0.0.0.0可以让其他电脑也能访问到该网站，
# port指定访问的端口。默认的host是127.0.0.1，port为5000
# debug默认为false，当=True 表示不重启app，可以正常调试
#处理视图函数,必须有返回值 1返回文本 2.返回html 3.接口 json数据（不能返回字典）
#flask模块中的request：请求上下文，客户端发送了请求给服务端，就发送了一个request对象。
#通过一系列的方法读取这个request对象中的内容（客户端传过来的；请求方法，path，请求参数,请求头信息）
'''
request.args请求参数,get类型，获取某一个参数的值，用get方法取具体的值
request.get_json() :post类型，入参为json字符串，
request.form：post类型，入参为表单类型，用get方法取具体的值
request.get_data():post类型，入参为text文件类型，默认的值是字节类型，
request.path请求路径
request.method请求方法
request.headers.get() 请求头信息,拿到token，token到底正不正确，然后再去数据库比较
    print(request.headers.get('token'))
    print(request.headers.get('cookie'))
    print(request.headers.get('Authorization'))
    print(request.headers.get('User-Agent'))
    
响应值里面：code，httpstatus，这个是前后端开发人员 内部约定的状态码 ,接口能正常请求成功，状态码200
 但是可能有些数据异常 
'''

#datas表示所有用户的数据，来自数据库
datas = [
    {'name': 'test1', 'from': '长沙','id':1,"gender":"boy"},
    {'name': 'test2', 'from': '上海','id':2,"gender":"boy"},
    {'name': 'test3', 'from': '深圳','id':3,"gender":"girl"},
    {'name': 'test4', 'from': '深圳','id':4,"gender":"girl"},
    {'name': 'test5', 'from': '深圳','id':5,"gender":"boy"},
]


@app.route('/')
def test():
    return 'Hello qingfeng，test!'

# @app.route('/test')
# def new():
#     return '''<html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>测试一下标题</title>
# </head>
# <body>
# <button> 这是一个按钮</button>
# </body>
# </html>'''
@app.route('/test')
def new():
    return render_template('qingfeng.html')


'''接口：获取所有的用户的接口，get
'''
import json
@app.route('/users',methods=['GET'])
def users():
    '''获取所有的用户
    limit:表示限制数量， 1 返回一条数据   非必填
    tab：表示类型， tab：boy 返回用户里面所有性别为男的用户信息   非必填
    参数异常的情况，添加各种返回提示信息
    '''
    canshu=request.args
    #多个参数都传了，需要放到第一个来判断,
    # 我想在tab为 girl的情况下，再返回限制条数
    # 我想在前10条数据，返回这10条里面tab为girl
    if 'tab' in canshu and 'limit' in canshu:  #如果用户传了limit参数,而且传了tab
        limit = canshu.get('limit')
        tab = canshu.get('tab')
        d = [data for data in datas if data["gender"] == tab]
        d=d[:int(limit)]
        return jsonify({"code":200,"users":d})


    if 'limit' in canshu: #如果用户传了limit参数
        limit = canshu.get('limit')
        d=datas[:int(limit)]  # L[:1]
        return jsonify({"code":200,"users":d})

    '''datas = [
    {'name': 'test1', 'from': '长沙','id':'1',"gender":"boy"},
    {'name': 'test2', 'from': '上海','id':'2',"gender":"boy"},
    {'name': 'test3', 'from': '深圳','id':'3',"gender":"girl"},
    {'name': 'test4', 'from': '深圳','id':'4',"gender":"girl"},
    {'name': 'test5', 'from': '深圳','id':'5',"gender":"boy"},
]'''

    if 'tab' in canshu:  # 如果用户传了limit参数
        tab = canshu.get('tab')
        # d=[]
        # for data in datas:
        #     if data["gender"]==tab:
        #         d.append(data)
        d=[data for data in datas if data["gender"]==tab]
        return jsonify({"code": 200, "users": d})


    else:  #没有传任何参数，默认返回所有的用户
        return jsonify({"code":200,"users":datas})  #返回的必须是一个json字符串,json对象  [],{}

@app.route('/user/<int:id>',methods=['GET'])
def user(id):
    '''获取单个用户
    id:通过用户请求传过来的id，传入视图函数'''
    d=[data for data in datas if data["id"] == id]
    if len(d)==0:#如果列表为空，说明没有满足的值
        return jsonify({"code":000,"msg":'没有此用户{}'.format(id)})
    return jsonify({"code":200,"id":d})

@app.route('/user',methods=['POST'])
def addUser():
    '''新增用户
    必传的参数：name，gender
    '''
    canshu=request.get_json()
    name=canshu['name']
    gender=canshu['gender']
    datas.append({"name":name,"gender":gender,'id':len(datas)+1,"city":"北京"})
    res={"code":200,"msg":"{}用户新增成功".format(canshu['name'])}
    return jsonify(res)

@app.route('/user',methods=['PUT'])
def editUser():
    '''编辑用户'''
    canshu=request.form
    #id=canshu.get('id')
    #phone=canshu.get('phone')
    #print(id,phone)

    name=canshu.get('name')
    id=int(canshu.get('id'))
    print(id,type(id))
    print(name,type(name))

    d = [data for data in datas if data["id"] == id] #
    if len(d) == 0:  # 如果列表为空，说明没有满足的值
        return jsonify({"code": 000, "msg": '编辑失败，没有此用户{}'.format(id)})
    else:
        d[0]['name']=name

        res={"code":200,"msg":"用户{}编辑成功".format(id)}
    return jsonify(res)
  '''
     [
    {'name': 'test1', 'from': '长沙','id':1,"gender":"boy"},
    {'name': 'test2', 'from': '上海','id':2,"gender":"boy"},
    {'name': 'test3', 'from': '深圳','id':3,"gender":"girl"},
    {'name': 'test4', 'from': '深圳','id':4,"gender":"girl"},
    {'name': 'test5', 'from': '深圳','id':5,"gender":"boy"},
]
    d=[{'name': 'test3', 'from': '深圳','id':3,"gender":"girl"},]
    '''
@app.route('/user/<int:id>',methods=['DELETE'])
def deletUser(id):
    '''删除用户'''
    #canshu=request.get_data()
    d = [data for data in datas if data["id"] == id]  #
    if len(d) == 0:  # 如果列表为空，说明没有满足的值
        return jsonify({"code": 000, "msg": '删除失败，没有此用户{}'.format(id)})
    else:
        datas.remove(d[0])
        res={"code":200,"msg":"用户{}删除成功".format(id)}
        return jsonify(res)
if __name__ == '__main__':
     app.run(host='0.0.0.0',port=8086,debug=True)
     '''列表生成式：[表达式，for 循环语句，然后是if语句]，返回的结果是一个新列表
     [data for data in datas if data["gender"]==tab]
      #1.循环一个列表，2.再加一个if判断，获取列表的满足条件的值，3.再添加到一个新的列表
     '''
     # l=[]
     # for i in range(1,11):
     #     if i %2!=0:
     #         l.append(i*i)#10以内的奇数的平方
     # print(l)
     #
     # d=[i*i for i in range(1,11) if i%2!=0]
     # print(d)

