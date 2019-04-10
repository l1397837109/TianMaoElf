from dao.MatterMode import matter,corpus,matter_session,box
from App import db

class matterCorpus():

    #获取事项列表
    def matterList(self):
        matter_list = matter.query.all()
        return matter_list


    #根据事项id查出提问语料
    def corpusList(self,mtId):
        corpus_list = corpus.query.filter_by(matterId=mtId).all()
        return corpus_list


    #插入会话数据
    def instSession(self,*args):
        print('---args---',args)
        boxOb = box.query.filter_by(boxName=args[0]).all()
        print(boxOb)
        ms = matter_session(boxId=boxOb[0].id,matterId=args[1],matterName=args[2],sessionId=args[3],sessionCount=args[4])
        db.session.add(ms)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(e)








mc = matterCorpus()
