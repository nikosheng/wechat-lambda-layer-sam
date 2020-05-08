# wechat-lambda-layer-sam

### Deploy in Serverless Application Repository


- Login AWS Console and navigate to `Serverless Application Repository` service.
- Search `enterprise-wechat-lambda-layer` in `Available Applications`
- Press `Deploy` button to deploy the lambda layer to your account
- Navigate to `Lambda` service and find out the layer is already deployed or not


### Usage

```
import json
import os
from wechat import Wechat
from alarm import Alarm

def handler(event, context):
    corpId = os.environ['CORPID']
    corpSecret = os.environ['CORPSECRET']
    wechat = Wechat(corpId, corpSecret)
    wxAlarm = Alarm(
        toUser = "@all",  #成员ID列表（消息接收者，多个接收者用‘|’分隔，最多支持1000个）。特殊情况：指定为@all，则向关注该企业应用的全部成员发送
        toParty = "",     #部门ID列表，多个接收者用‘|’分隔，最多支持100个。当touser为@all时忽略本参数
        toTag = "",       #标签ID列表，多个接收者用‘|’分隔，最多支持100个。当touser为@all时忽略本参数
        agentId = 1000002,
        title = "AWS 告警信息",
        description = "<div class=\"grey\">{0}</div> <div class=\"highlight\">{1}</div>".format(event['Records'][0]['Sns']['Timestamp'], event['Records'][0]['Sns']['Subject']),
        url = "URL"
    )
    body = wechat.send_msg(wxAlarm)

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
```



Happy Building!  
Niko (nikosheng@gmail.com)