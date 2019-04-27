from wxpy import *
import load
import wx_reply


# 实例化一个机器人
bot = Bot(cache_path=False) # cache_path 设置当前缓存，可以短时间内不必在扫码登陆
# 加载配置信息到机器人
# load.load_config_to_bot(bot)

"""注册好友请求类消息"""
@bot.register(msg_types=FRIENDS)
# 自动接收验证信息中包含'wxpy'的好友请求
def auto_accept_friends(msg):
    # 判断好友请求中的验证文本
    if 'wxpy' in msg.text.lower():
        # 接受好友(msg.card 为该请求的用户对象)
        new_friend = bot.accept_friend(msg.card)
        new_friend.send('我自动接受了你的请求！')

"""自动回复好友消息"""
@bot.register(chats=Friend)
def friend_auto_reply(msg):
    # if not msg.bot.is_frined_auto_reply:
    #     return None
    if msg.type == TEXT:
        wx_reply.auto_reply(msg)
        return None
    elif msg.type == RECORDING:
        return '不停'
    else:
        pass

# 交互模式，阻塞线程，使程序一直运行
embed()
