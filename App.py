#引入框架配置文件
import Config
#引入框架包
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
#创建应用对象
TmApp = Flask(__name__)
#app示例添加配置
TmApp.config.from_object(Config)
#创建数据库实例对象
db = SQLAlchemy(TmApp)
Session(TmApp)
#导入视图
import view.IntentionView



