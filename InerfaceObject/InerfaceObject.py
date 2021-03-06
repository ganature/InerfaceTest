# coding=utf-8

from Common.RequestsLibrary import RequestsLibrary
from InerfaceObject.InerfaceConfig import *
import base64
import hashlib
import json


class InerfaceObject:
    """
    接口测试封装Request和加密
    """

    def __init__(self):
        self.base_url = LOGIN_INERFACE_BASEURL

    @property
    def request(self):
        request = RequestsLibrary ()
        return request

    def generate_login_key(self, *args):
        # type: (object) -> object
        '''
        base64加密登录参数，生成key
        :param parm:parm为字典类型，登录参数为字典的key，登录参数值为字典的values
        example：parm={'loginName':'test','password':'test'}
        :return:
        '''

        return base64.encodestring (','.join (args[0]))

    def generate_sign(self, args):
        '''
        MD5加密，生成sign
        :param signparm:为字典类型，接口参数为字典的key，参数值为字典的values
        example：
        :return:
        '''
        signset = []
        sign = args.keys ()
        sign.sort ()
        for si in sign:
            signset.append (si + args[si])
        s = ''.join (signset)
        m = hashlib.md5 ()
        m.update (s)
        return m.hexdigest ().upper ()

    def get_request(self, url, cookies=None):
        result = self.request.get_request (url, cookies)
        return result

    def I_put_request(self, url, parm=None):
        result = self.request.put_request (url)
        return result

    def I_post_request(self, url, parm=None):
        result = self.request.post_request (url)
        return result

    def join_login_url(self, *args):
        """
        拼接登录url
        :param args:
        :return:
        """
        if isinstance (args, tuple):
            key = self.generate_login_key (*args)
            return self.base_url + key
        elif isinstance (args, dict):
            key = self.generate_login_key (args.values ())
            return self.base_url + key
        elif isinstance (args, str):
            j = json.loads (args)
            key = self.generate_login_key (j.values ())
            return self.base_url + key

    def join_url(self, args):
        """
        生成sign，拼接请求的包含sign参数字典
        :param args:
        :return:
        """
        urls = []
        sign = self.generate_sign (args)
        args.update ({'sign': sign})
        items = arg.items ()
        for i in items:
            (key, value) = i
            temp_str = key + '=' + value
            urls.append (temp_str)
        return '&'.join (urls)


if __name__ == '__main__':
    l = InerfaceObject ()
    arg = {'LoginName': 'qxd', 'password': '123'}
    a = l.join_url (arg)
