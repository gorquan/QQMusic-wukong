# -*- coding: utf-8-*-
# author: gorquan
# QQ音乐插件

from robot.sdk.AbstractPlugin import AbstractPlugin
from robot.sdk import unit
from robot import config, logging

logger = logging.getLogger(__name__)

class Plugin(AbstractPlugin):
    
    # 判断用户指令是否适合插件处理
    def isValid(self, text, parsed):
        # Todo: 做判断，多种情况进入插件
        return unit.hasIntent(parsed, 'MUSICINFO')

    # 执行处理
    def handle(self, text, parsed):
        # 分情况判断
        slots = unit.getSlots(parsed, 'MUSICINFO')
        account_info = self.getUserInfo()
        # 情况：第一次登录/已经登录
        if (account_info['status']):
            self.say('请先配置你的账号密码哦', cache=True)
        else:
            # 登录
            account_cookie = ''
        # todo: 处理情况
        # 1. 知道歌手不知道歌曲名
        # 2. 知道歌曲名不知道歌手
        # 3. 知道歌手和歌曲名
        # 4. 播放歌单
        # 5. 播放我喜欢
        # 6. 播放FM

    # 获取用户账号密码
    # TODO: 空判断？
    def getUserInfo(self):
        result = dict()
        account = config.get('account', '0')
        password = config.get('password', '0')
        if (account == '0' || 'password' == '0'):
            result['status'] = False
            logger.info('无法取得用户信息')
        else:
            result['status'] = True
            result['account'] = account
            result['password'] = password
            logger.debug('取得用户信息')
        return result
            
    # 获取cookie
    def getUserCookie():
        pass
    


    

    

