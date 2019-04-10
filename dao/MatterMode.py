from App import db

#事项数据模型
class matter(db.Model):
    __tablename__ = 'matter'

    id = db.Column(db.Integer,primary_key=True)
    matterId  = db.Column(db.String(50),unique=True,nullable=False)
    matterName = db.Column(db.String(50),unique=True)
    matterDesc = db.Column(db.Text)
    creaTime = db.Column(db.DateTime)
    matterType = db.Column(db.String(30))

    def __repr__(self):
        return 'matter: %s %s %s %s %s %s' % (self.id, self.matterId, self.matterName, self.matterDesc, self.matterType, self.creaTime)



#语料数据模型
class corpus(db.Model):
    __tablename__ = 'corpus'

    id = db.Column(db.Integer,primary_key=True)
    questions = db.Column(db.String(255))
    answer = db.Column(db.String(255))
    orderNumber = db.Column(db.Integer)
    matterId = db.Column(db.String(50))
    creaTime = db.Column(db.DateTime)

    #在定义模型时声明排序方式
    __mapper_args__ = {
        'order_by':orderNumber.asc()
    }

    def __repr__(self):
        return 'corpus: %s %s %s %s %s %s' % (self.id, self.questions, self.answer, self.orderNumber, self.matterId, self.creaTime)



#会话内容数据模型
class matter_session(db.Model):
    __tablename__ = 'matter_session'

    id =  db.Column(db.Integer,primary_key=True)
    boxId = db.Column(db.String(50))
    matterId = db.Column(db.String(50))
    matterName = db.Column(db.String(50))
    sessionId = db.Column(db.String(50))
    sessionCount = db.Column(db.Text)
    creaTime = db.Column(db.DateTime)

    def __repr__(self):
        return 'matter_seesion: %s %s %s %s %s %s %s' % (self.id,self.boxId,self.matterId,self.matterName,self.sessionId,self.sessionCount,self.creaTime)




#音箱实体类
class box(db.Model):
    __tablename__ = 'box'

    id = db.Column(db.Integer,primary_key=True)
    boxName = db.Column(db.String(50))
    creaTime = db.Column(db.DateTime)
    boxType = db.Column(db.String(50))


