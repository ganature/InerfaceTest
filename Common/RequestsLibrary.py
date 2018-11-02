# coding=utf-8
import requests
import json



class RequestsLibrary (object):
    """
    封装Requests库
    """

    def __init__(self):
        self.session=requests.Session()


    def _create_session(self,headers,
            cookies,
            auth,
            timeout,
            max_retries,
            backoff_factor,
            proxies,
            verify,
            debug,
            disable_warnings):
        """
        创建session
        :param headers:
        :param cookies:
        :param auth:
        :param timeout:
        :param max_retries:
        :param backoff_factor:
        :param proxies:
        :param verify:
        :param debug:
        :param disable_warnings:
        :return:
        """



if __name__ == '__main__':
    r = requests.session ()
    result = r.get ('http://www.tietonggroup.com/ttsd/publicNumber/login?key=dGlhbmhjLDExMTExMQ==')
    print (type (json.loads (result.content)))
    content = json.loads (result.content)
    token = content['data']['token']
    r = RequestsLibrary ()
