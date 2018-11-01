# coding=utf-8

from  InerfaceObject.InerfaceObject import InerfaceObject
from InerfaceObject.InerfaceConfig import *
import json

class SysuserInerface:

    def __init__(self):
        self.sys=InerfaceObject()

    def get_token(self,result):
        """
        获取返回结果中的token
        :param result:
        :return:
        """
        r=json.loads (result.content)
        return r['data']['token']

    def get_status(self,result):
        """
        获取返回状态码
        :param result:
        :return:
        """
        r=json.loads (result.content)
        return r['status']

    def admin2_login(self,*args):
        """
        二级管理员登录，返回token
        :return: token
        """
        # 拼接访问的URL
        url=self.sys.join_login_url (*args)
        # 发送GET请求
        result=self.sys.I_get_request (url)
        token=self.get_token(result)
        return token

    def admin3_login(self,*args):
        """
        三级管理员登录，返回token
        :return:
        """
        # 拼接访问的URL
        url=self.sys.join_login_url (*args)
        # 发送GET请求
        result=self.sys.I_get_request (url)
        token=self.get_token (result)
        return token

    def add_sysuser(self,admin2,admin3):
        """
        增加三级管理员
        :param admin2: 登录二级管理员的账号和密码
        :param admin3: 新增三级管理员的账号信息
        :return: 请求返回结果码
        """
        admin2_token=self.admin2_login(admin2)
        admin3.updata ({'token': admin2_token})
        url=SYSUSER_CREAT_INERFACE+self.sys.join_url(admin3)
        result=self.sys.I_get_request(url)
        status=self.get_status(result)
        return status

    def add_user(self,admin3,):
        """
        增加账号
        :return:
        """
        #新增三级管理员
        admin3_token=self.admin3_login()


    def query_user(self):
        """
        查询用户，
        :return:
        """
    def add_group(self):
        """
        新增群组
        :return:
        """
    def query_group(self):
        """
        查询群组
        :return:
        """
