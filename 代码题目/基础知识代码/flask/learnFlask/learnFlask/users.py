'''用户相关的接口'''
from flask import Blueprint
from flask import request,jsonify
bp = Blueprint('user',__name__,url_prefix='/') #定义一个蓝图
datas = [{'name': '张三', 'from': '长沙','id':'1',"gender":"boy"},
    {'name': '李四', 'from': '上海','id':'2',"gender":"boy"},
    {'name': '王五', 'from': '深圳','id':'3',"gender":"girl"},
         {'name': '老六', 'from': '深圳','id':'4',"gender":"boy"},]

@bp.route('/users',methods=['GET'])
def users():
        canshu=request.args

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

@bp.route('/user',methods=['POST'])
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