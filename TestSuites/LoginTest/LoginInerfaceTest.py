# coding=utf-8

from TestSuites.Main import MainTest
from InerfaceObject.InerfaceObject import InerfaceObject
from ddt import ddt, file_data
import json
from TestData.DataConfig import DataConfig


def get_test_data(module_name, test_case_name):
    d = DataConfig (filename='../../TestData/DataSource.xlsx')
    parm_dict = d.get_TestCase_Parmerner (module_name, test_case_name)
    return parm_dict


@ddt
class LoginInerTest (MainTest):
    '''
    登录接口测试类
    '''

    @property
    def request(self):
        request = InerfaceObject ()
        return request

    @file_data ('LoginTest.json')
    def test_normal_login(self, input, out):
        '''
        登录接口测试用例
        :param userName: 登录用户名
        :param password: 登录密码
        :return:
        '''
        # 拼接访问的URL
        url = self.request.join_login_url (input)
        # 发送GET请求
        result = self.request.I_get_request (url)
        r = json.loads (result.content)
        exception = out['exception']
        self.assertEqual (r['status'], int (exception))

    def normal_login(self, *args):
        '''
        登录接口测试用例
        :param userName: 登录用户名
        :param password: 登录密码
        :return:token:返回登录成功的token
        '''
        # 拼接访问的URL
        url = self.request.join_login_url (*args)
        # 发送GET请求
        result = self.request.I_get_request (url)
        r = json.loads (result.content)
        return r['data']['token']


if __name__ == '__main__':
    # suite=unittest.TestLoader ().loadTestsFromTestCase (LoginInerTest)
    # unittest.TextTestRunner (verbosity=2).run (suite)
    # data={1:1,2:2,3:3}
    # for i, elem in enumerate(data):
    #     if isinstance(data, dict):
    #         key, value = elem, data[elem]
    #         print key,value

    pass
