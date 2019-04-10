from App import TmApp
from flask import jsonify,send_from_directory,request
from .BusinessProcessService import bps
import MatterEntity

@TmApp.route('/',methods=['GET'])
def hello_world():
    m = MatterEntity.mc.corpusList('XC_SX002')
    for i in m[:-1]:
        print(i.questions)
    return '天猫接口正常运行'

#文件验证
@TmApp.route('/aligenie/file.txt',methods=['GET'])
def aligenie():
    return send_from_directory('./aligenie','file.txt',as_attachment=True)


#主要逻辑处理
@TmApp.route('/index',methods=['POST'])
def index():
    resData = bps.matter(request.get_data(as_text=True))
    return jsonify(resData)