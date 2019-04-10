import requests
import json
# 定义全局flag



class dd():
    def __init__(self):
        self.flag = 0
        self.juflag = 1

    def fv(self):

        self.flag += 1
        print(self.flag)

    def fee(self):
        self.flag += 1
        print(self.flag)

    def jjjj(self):
        aa = {'sessionId': 'df45f440-b505-4f2f-b9b5-9f229d0cec13', 'utterance': '最多跑一次','skillId': 25199, 'skillName': '1Call办', 'intentId': 27974, 'intentName': '进入会话', 'requestData': {'city': '杭州市', 'userOpenId': 'QkHEdtFniTA5RWu6b4bJ9vAhyP7TR6LdqZAlRHOWsj0=', 'deviceOpenId': 'TKc0U+37jXavOwmUXjhi8iEJVLLeBfsHdctXIxk/Kst994eNmZO8MA=='}, 'slotEntities': [], 'botId': 10, 'domainId': 22542, 'requestId': '20190318170044714-88878140'}
        ff = json.dumps(aa)
        b = requests.post('http://localhost:5000/index',data=ff).text
        print(b)

    def jkjk(self):
        a = ['i']
        if a[:-1]:
            print(a[:-1])
        else:
            print(a)


    def uiui(self):
        i = 10%2
        print(i)





d = dd()

d.uiui()