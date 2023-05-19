from flask import Flask,render_template,jsonify
from flask import request
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

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
#通过一系列的方法读取这个request对象中的内容（请求方法，path，请求参数,请求头信息）
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
'''

datas = [{'name': '张三', 'from': '长沙','id':'1'},
    {'name': '李四', 'from': '上海','id':'2'},
    {'name': '王五', 'from': '深圳','id':'3'},]


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
    '''获取所有的用户'''
    d={
        "code": 200,
        "data":[
            {
                "name1":"test1",
                "rank":"putong"
            },
            {
                "name2":"test2",
                "rank":"vip"

    },
            {
                "name3":"test3",
                "rank":"vvip"
            }
        ],
}
    #d=json.dumps(d)
    canshu=request.args
    # print(canshu)
    # print(request.path)
    # print(request.method)
    limit=canshu.get('limit')
    tab=canshu.get('tab')
    d=jsonify(d)
    return d

@app.route('/users/<int:id>',methods=['GET'])
def user(id):
    '''获取单个用户
    id:通过用户请求传过来的id，传入视图函数'''
    print(id)
    res={"code":201,"id":id}
    return jsonify(res)

@app.route('/addUser',methods=['POST'])
def addUser():
    '''新增用户'''
    canshu=request.get_json()
    #print(type(canshu),canshu)
    res={"code":200,"msg":"{}用户新增成功".format(canshu['username'])}
    return jsonify(res)

@app.route('/editUser',methods=['POST'])
def editUser():
    '''编辑用户'''
    canshu=request.form
    id=canshu.get('id')
    phone=canshu.get('phone')
    print(id,phone)
    res={"code":200,"msg":"用户编辑成功"}
    return jsonify(res)

@app.route('/deleteUser',methods=['POST'])
def deletUser():
    '''删除用户'''
    canshu=request.get_data()
    print(type(canshu),canshu,)
    print(type(str(canshu)))
    res={"code":200,"msg":"用户删除成功"}
    return jsonify(res)
if __name__ == '__main__':
     app.run(host='0.0.0.0',port=8086,debug=True)
