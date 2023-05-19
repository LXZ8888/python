from flask import Flask,render_template,jsonify

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
    d={
        "code": 200,
        "data":[
            {
                "name":"test1"
            },
            {
                "name":"清风"
            }
        ],
}
    #d=json.dumps(d)
    d=jsonify(d)
    return d


if __name__ == '__main__':
     app.run(host='0.0.0.0',port=8086,debug=True)
