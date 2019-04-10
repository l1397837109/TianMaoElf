import json
from MatterEntity import mc
from flask import session

class BusinessProcess():
    def __init__(self):
        #全局事项id
        self.flag = ''
        #全局语料下标
        self.juflag = 1
        #全局会话内容
        self.sessionData = []
        #全局事项id和事项名称
        self.matterInfo = []

    #处理函数
    def matter(self,reqData):
        data =  json.loads(reqData)
        print(data)
        # 进入会话判断
        if data['utterance'] == '依靠助手':
            reply = '请问您需要办理什么业务？'
            resultType = 'CONFIRM'
            self.flag = ''
            self.juflag = 1
        # 选择业务后标记flag
        elif self.flag == '':
            reply = ''
            for m in mc.matterList():
                if data['slotEntities'][0]['standardValue'] == m.matterName:
                    #会话存入用户输入的事项名称
                    self.sessionData.append(data['utterance'])
                    #全局事项信息存入id和名称
                    self.matterInfo.append(m.matterId)
                    self.matterInfo.append(m.matterName)
                    # 获取提问语料数据对象列表
                    cpList = mc.corpusList(m.matterId)
                    #长度大于1表示有提问语料
                    if len(cpList) > 1:
                        #存入天猫回答的第一个语料
                        self.sessionData.append(cpList[0].questions)
                        reply = cpList[0].questions
                        resultType = 'CONFIRM'
                        # 业务标记
                        self.flag = m.matterId
                    #长度等于1表示单次会话，直接返回办理方法
                    elif len(cpList) == 1:
                        # 存入天猫回答的第一个语料
                        self.sessionData.append(cpList[0].questions)
                        reply = cpList[0].questions
                        resultType = 'RESULT'
                    #没有语料直接返回事项描述
                    else:
                        # 存入天猫回答的事项描述
                        self.sessionData.append(cpList[0].questions)
                        reply = m.matterDesc or '无描述'
                        resultType = 'RESULT'
            #如果没有找到事项返回提示
            if reply == '':
                reply = '事项库未配置该事项'
                resultType = 'RESULT'
        # flag标记后进行是否逻辑判断
        else:
            if data['slotEntities'][0]['standardValue'] == '是':
                #存入回答是
                self.sessionData.append(data['utterance'])
                try:
                    reply = mc.corpusList(self.flag)[:-1][self.juflag].questions
                    #存入天猫的下一个问题
                    self.sessionData.append(reply)
                    resultType = 'CONFIRM'
                    self.juflag += 1
                except:
                    reply = mc.corpusList(self.flag)[-1].questions
                    #存入天猫的回复
                    self.sessionData.append(reply)
                    resultType = 'RESULT'
                    self.flag = ''
                    self.juflag = 1
            else:
                # 存入回答否
                self.sessionData.append(data['utterance'])
                reply = mc.corpusList(self.flag)[self.juflag].answer
                # 存入天猫的回复
                self.sessionData.append(reply)
                resultType = 'RESULT'
                self.flag = ''
                self.juflag = 1

        #打印会话
        if resultType == 'RESULT':
            print('-------------------完成一次会话------------------')
            print(self.sessionData)
            #插入数据库
            mc.instSession(data['botId'],self.matterInfo[0],self.matterInfo[1],data['sessionId'],'|'.join(self.sessionData))
            self.sessionData.clear()
            self.matterInfo.clear()
        #组装返回json数据
        data_dict = {
            "returnCode": "0",
            "returnErrorSolution": "",
            "returnMessage": "",
            "returnValue": {
                "reply": reply,
                "resultType": resultType,
                "actions": [
                    {
                        "name": "audioPlayGenieSource",
                        "properties": {
                            "audioGenieId": "123"
                        }
                    }
                ],
                "properties": {},
                "executeCode": "SUCCESS",
                "msgInfo": ""
            }
        }

        return data_dict


bps = BusinessProcess()
