# -*- coding: UTF-8 -*-
#######################
# 更多的企业微信API可以参考https://work.weixin.qq.com/api/doc/90000/90135/90250
#######################
import requests
import json
from alarm import Alarm

class Wechat:
    s = requests.session()
    token = None

    def __init__(self, corpId, corpSecret):
        self.corpId = corpId
        self.corpSecret = corpSecret
        self.token = self.get_token(corpId, corpSecret)
        print("token is " + self.token)

    # 获取Access Token
    def get_token(self, corpId, corpSecret):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={0}&corpsecret={1}".format(corpId, corpSecret)
        rep = self.s.get(url)
        if rep.status_code == 200:
            return json.loads(rep.content)['access_token']
        else:
            print("request failed.")
            return None

    # 发送企业微信消息
    def send_msg(self, wxAlarm):
        url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=" + self.token
        header = {
            "Content-Type": "application/json"
        }
        form_data = {
            "touser": wxAlarm.toUser,
            "toparty": wxAlarm.toParty,
            "totag": wxAlarm.toTag,
            "msgtype": "textcard",
            "agentid": wxAlarm.agentId,
            "textcard": {
                "title": wxAlarm.title,
                "description": wxAlarm.description,
                "url": wxAlarm.url,
                "btntxt": "More"
            },
            "safe": 0
        }
        rep = self.s.post(url, data=json.dumps(form_data).encode('utf-8'), headers=header)
        if rep.status_code == 200:
            return json.loads(rep.content)
        else:
            print("request failed.")
            return None


if __name__ == '__main__':
   pass

