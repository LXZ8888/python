'''用例相关的接口'''
from flask import Blueprint
bp = Blueprint('testcase',__name__,url_prefix='/testcase/') #定义一个用例模块的蓝图

@bp.route('/',)
def index():
    return "用例首页"

@bp.route('detail/')
def profile():
    return "用例详情"