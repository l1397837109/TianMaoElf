#mysql数据库地址
SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://lxr:123456@172.16.8.10/smart_speakers'
#数据库跟踪修改
SQLALCHEMY_TRACK_MODIFICATIONS = False
#调试模式
DEBUG = False
#flask_session配置
SESSION_TYPE = 'filesystem' #类型
#SESSION_FILE_DIR = '/sessions' #文件目录
SESSION_FILE_THRESHOLD = 50 # 存储session的个数如果大于这个值时，就要开始进行删除了
SESSION_FILE_MODE = 384 # 文件权限类型
SESSION_PERMANENT = False # 如果设置为True，则关闭浏览器session就失效。
SESSION_USE_SIGNER = False # 是否对发送到浏览器上session的cookie值进行加密
