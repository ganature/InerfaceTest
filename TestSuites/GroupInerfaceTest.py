# coding=utf-8
from .Main import MainTest
from ddt import ddt
from InerfaceObject.InerfaceObject import InerfaceObject
from TestSuites.LoginTest import LoginInerfaceTest

@ddt
class GroupInerfaceTest(MainTest):

    @property
    def request(self):
        request=InerfaceObject ()
        return request

    @property
    def login(self):
        login=LoginInerfaceTest ()
        return login

    def test_add_group(self,input,out):
        """
        测试增加群组接口
        :param input:
        :param out:
        :return:
        """
        pass

    def test_edit_group(self,input,out):
        """
        测试修改群组接口
        :param input:
        :param out:
        :return:
        """
        pass

    def test_delete_group(self,input,out):
        """
        测试删除群组接口
        :param input:
        :param out:
        :return:
        """
        pass