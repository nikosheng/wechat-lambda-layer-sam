# -*- coding: UTF-8 -*-

class Alarm:

    def __init__(self, toUser, toParty, toTag, agentId, title, description, url):
        self.toUser = toUser #成员ID列表（消息接收者，多个接收者用‘|’分隔，最多支持1000个）。特殊情况：指定为@all，则向关注该企业应用的全部成员发送
        self.toParty = toParty #部门ID列表，多个接收者用‘|’分隔，最多支持100个。当touser为@all时忽略本参数
        self.toTag = toTag #标签ID列表，多个接收者用‘|’分隔，最多支持100个。当touser为@all时忽略本参数
        self.agentId = agentId #企业应用的id，整型。企业内部开发，可在应用的设置页面查看
        self.title = title #标题，不超过128个字节，超过会自动截断
        self.description = description #描述，不超过512个字节，超过会自动截断
        self.url = url #点击后跳转的链接

if __name__ == '__main__':
    pass