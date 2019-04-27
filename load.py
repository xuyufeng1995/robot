import wxpy
import config


def load_config_to_bot(bot):
    """加载配置项"""
    bot_status = "机器人登陆成功！！！"

    # 定义远程管理主人
    master = wxpy.search_friend(bot, config.bot_master_name)
    if master:
        bot.master = master
        bot_status += '\n机器人管理员成功设置为：「{0}」，这里查看管理员命令手册->' \
                      'https://github.com/pig6/wxrobot\n\n'.format(config.bot_master_name)
