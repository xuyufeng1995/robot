import json
import requests
from wxpy import *
import config

"""免费申请图灵机器人，获取API地址"""
tuling = Tuling(api_key=config.tuling_api_key)

def auto_reply(msg):
    """回复消息，并返回答复文本"""
    return tuling.do_reply(msg)

if __name__ == '__main__':
    """
        测试图灵机器人
        报40007错误的原因打开了密钥开关，务必关上    坑
    """
    apikey = 'd552c69086154c048d9962258e1d47c0'
    api_url = 'http://www.tuling123.com/openapi/api'
    word = '你好'
    data = {'key':apikey,'userInfo':word.encode('utf8')}
    req = requests.post(api_url,data=data).text
    print(req)
    replys = json.loads(req)['text']
    print(replys)
