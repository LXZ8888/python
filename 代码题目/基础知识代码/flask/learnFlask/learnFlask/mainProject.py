from flask import Flask,render_template,jsonify
from flask import request
import testcase,users
app = Flask(__name__) #主程序
app.config['JSON_AS_ASCII'] = False
app.register_blueprint(users.bp) #注册用户蓝图
app.register_blueprint(testcase.bp) #注册用例蓝图

if __name__ == '__main__':
     app.run(host='0.0.0.0',port=8086,debug=True)
