# coding=utf-8

from InerfaceObject.InerfaceObject import InerfaceObject
from InerfaceObject.InerfaceConfig import *
from .LoginTest.LoginInerfaceTest import LoginInerTest
from TestCases.SysuserInerface import SysuserInerface
from .Main import MainTest
import ddt
import json
import unittest
import HTMLTestRunner



class SysuserInerTest (unittest.TestCase):

    @property
    def request(self):
        request=SysuserInerface ()
        return request

    @property
    def login(self):
        login=LoginInerTest ()
        return login

    @ddt.data([3, 2], [4, 3], [5, 3])
    @ddt.unpack
    def test_list_extracted_into_arguments(self, first_value, second_value):
        self.assertTrue(first_value > second_value)

    @ddt.file_data ('test_add_sysuser.json')
    def test_add_sysuser(self, setup,input,out,teardown):
        """
        测试新增三级管理员接口
        :param setup: 初始化参数 登录二级管理员
        :param input: 测试输入参数
        :param out: 测试期望输出
        :param teardown: 还原测试环境
        :return:
        """
        result=self.request.add_sysuser(setup,input)
        exception=out['exception']
        self.assertEqual (int (result), int (exception))

    @ddt.file_data('test_error_add_parm.json')
    def test_error_add_parm(self,setup,input,out,teardown):
        """
        新增三级管理员参数错误测试用例
            1、参数拼写错误
            2、缺少参数错误
            3、多余参数错误
        :return:
        """
        result=self.request.add_sysuser (setup, input)
        exception=out['exception']
        self.assertEqual (int (result), int (exception))



    @ddt.file_data('test_edit_sysuser.json')
    def test_edit_sysuser(self,setup,input,out,teardown):
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
