# coding=utf-8

from Common.RequestsLibrary import RequestsLibrary
from InerfaceConfig import *
import base64
import hashlib
import json
import MySQLdb


class InerfaceObject:
    """

    """

    def __init__(self):
        self.base_url=LOGIN_INERFACE_BASEURL
        # self.con=MySQLdb.connect(
        #     host=MySQL_HOST,
        #     user=MySQL_USER,
        #     passwd=MySQL_PASSWORD,
        #     db=MySQL_DB
        # )
        # self.cur=self.con.cursor(cursorclass=MySQLdb.cursors.DictCursor)

    @property
    def request(self):
        request=RequestsLibrary ()
        return request

    def mysql(self):
        pass
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
        signset=[]
        sign=args.keys ()
        sign.sort ()
        for si in sign:
            signset.append (si + args[si])
        s=''.join (signset)
        m=hashlib.md5 ()
        m.update (s)
        return m.hexdigest ().upper ()

    def I_get_request(self, url,  cookies=None):
        result=self.request.get_request (url,cookies)
        return result

    def I_put_request(self, url, parm=None):
        result=self.request.put_request (url)
        return result

    def I_post_request(self, url, parm=None):
        result=self.request.post_request (url)
        return result

    def join_login_url(self, *args):
        """
        拼接登录url
        :param args:
        :return:
        """
        if isinstance (args, tuple):
            key=self.generate_login_key (*args)
            return self.base_url + key
        elif isinstance (args, dict):
            key=self.generate_login_key (args.values ())
            return self.base_url + key
        elif isinstance (args, str):
            j=json.loads (args)
            key=self.generate_login_key (j.values ())
            return self.base_url + key

    def join_url(self, args):
        """
        生成sign，拼接请求的包含sign参数字典
        :param args:
        :return:
        """
        sign=self.generate_sign (args)
        args.update({'sign':sign})
        return args


if __name__ == '__main__':
    l=InerfaceObject ()

    a=l.generate_sign ({'a': '1', 'c': '3', 'b': '2'})
    print a
