# coding=utf-8

from InerfaceObject.InerfaceObject import InerfaceObject
from InerfaceObject.InerfaceConfig import *
from LoginTest.LoginInerfaceTest import LoginInerTest
from Main import MainTest
import ddt
import json
import unittest
import HTMLTestRunner


@ddt.ddt
class SysuserInerTest (MainTest):

    @property
    def request(self):
        request=InerfaceObject ()
        return request

    @property
    def login(self):
        login=LoginInerTest ()
        return login

    @ddt.file_data ('test_add_sysuser.json')
    def test_add_sysuser(self, setup,input,out,teardown):
        """
        测试新增三级管理员接口
        :param loginName: 新增三级管理员账号
        :param password: 新增三级管理员密码
        :param exception: 期望返回状态码
        :param name: 新增三级管理员名字
        :return:
        """
        # 登录二级管理员，获取token
        token=self.login.normal_login (LOGIN_SYSUSER_PARM.values ())
        # 生成请求参数字典
        input.updata ({'token': token})
        # 生成sign，参数字典加sign值
        args=self.request.join_url (input)
        # 拼接url
        url=SYSUSER_CREAT_INERFACE % dict (
            token=args['token'],
            sign=args['sign'],
            loginName=args['loginName'],
            password=args['password'],
            name=args['name']
        )
        result=self.request.I_get_request (url)
        r=json.loads (result.content)
        exception=out['exception']
        self.assertEqual (int (r['status']), int (exception))

    @ddt.file_data('test_error_add_parm.json')
    def test_error_add_parm(self,input,out):
        """
        新增三级管理员参数错误测试用例
            1、参数拼写错误
            2、缺少参数错误
            3、多余参数错误
        :return:
        """
        print input,out
        pass

    @ddt.file_data('test_edit_sysuser.json')
    def test_edit_sysuser(self,loginName, password, exception, name):
        # 登录二级管理员，获取token
        token=self.login.normal_login (LOGIN_SYSUSER_PARM.values ())
        # 生成请求参数字典
        parm=dict (zip (SYSUSER_EDIT_INERFACE_PARM, [token, loginName, password, name]))
        # 生成sign，参数字典加sign值
        args=self.request.join_url (parm)
        # 拼接url
        url=SYSUSER_EDIT_INERFACE% dict (
            token=args['token'],
            sign=args['sign'],
            loginName=args['loginName'],
            password=args['password'],
            name=args['name']
        )
        print url
        result=self.request.I_get_request (url)
        r=json.loads (result.content)
        self.assertEqual (int (r['status']), int (exception))

    @ddt.file_data('test_edit_sysuser.json')
    def test_error_edit_parm(self):
        """
        编辑三级管理员参数错误测试用例
            1、参数拼写错误
            2、缺少必填参数
            3、选填参数为空
            4、
        :return:
        """
        pass

    def runTest(self):
        pass


# if __name__ == '__main__':
#     unittest.main ()
