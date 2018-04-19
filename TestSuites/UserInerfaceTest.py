# coding=utf-8
from Main import MainTest
from InerfaceObject.InerfaceConfig import *
from InerfaceObject.InerfaceObject import InerfaceObject
from LoginTest.LoginInerfaceTest import LoginInerTest
from ddt import ddt,file_data,data

@ddt
class UserInerfaceTest(MainTest):
    @property
    def request(self):
        request=InerfaceObject ()
        return request

    @property
    def login(self):
        login=LoginInerTest ()
        return login

    @file_data('test_add_user.json')
    def test_add_user(self,input,out):
        """
        测试增加用户接口测试用例
        :param input:
        :param out:
        :return:
        """
        pass

    @file_data ('test_edit_user.json')
    def test_edit_user(self, input, out):
        """
        测试修改用户接口测试用例
        :param input:
        :param out:
        :return:
        """
        pass

    @file_data ('test_query_user.json')
    def test_query_user(self, input, out):
        """
        测试查询用户接口测试用例
        :param input:
        :param out:
        :return:
        """
        pass