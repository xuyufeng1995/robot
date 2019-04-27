import tuling_robot

def auto_accept_frinds(msg):
    new_friend = msg.card.accept()
    # 向新的好友发送消息
    new_friend.send("我已自动接受了你的好友请求")


def auto_reply(msg):
    """自动回复"""
    keyword_reply(msg) or tuling_reply(msg)


def keyword_reply(msg):
    """关键字回复"""
    if '你叫啥' in msg.text or '你叫什么' in msg.text:
            return msg.reply('大佬')
    pass


def tuling_reply(msg):
    """图灵机器人自动回复"""
    tuling_robot.auto_reply(msg=msg)
