"""项目配置"""
tuling_api_key = 'd552c69086154c048d9962258e1d47c0'

# 自动回复
is_friend_auto_reply = True
is_group_reply = True # 群中是否自动回复
is_group_at_reply = True # 上一项必须先开启这个

# 机器人主人
bot_master_name = '徐宇峰'

# 监听某些好友群聊,如老板
is_listen_friend = False
listen_fiend_names = 'honey' # 需要监听人的名称，适用备注名更加安全，允许多个用|分隔，如:主管|项目经理
listen_fiend_groups = 'Python新手交流' # 在这些群里监听好友说的话，匹配模式：包含‘唯一集团工作群’的群

# 转发至消息群

