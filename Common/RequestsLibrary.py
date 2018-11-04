# coding=utf-8
import requests
import json
from Common.Log import load_my_logging_cfg

from requests.packages.urllib3.util import Retry

logger=load_my_logging_cfg()

class RequestsLibrary(object):
    """
    封装Requests库
    """

    def __init__(self):
        pass
    @property
    def get_session(self):
        return requests.session ()

    def get_request(self, url,parm):
        return self.get_session.get (url)

    def post_request(self, url):
        return self.get_session.post (url)

    def put_request(self, url):
        return self.get_session.put (url)

    def delete_request(self, url):
        return self.get_session.delete (url)

class HttpClient(object):
    """
    封装Requests库
    """

    def __init__(self, headers=None, cookies=None, max_retries=1):
        """
        初始化requests.Session对象
        :param headers:
        :param cookies:
        :param max_retries:
        """
        self.session = requests.Session()

        logger.info('创建Session对象')
        if headers:
            self.session.headers.update(headers)
            logger.info('Session headers using: %s'%headers)
        try:
            max_retries = int(max_retries)
        except ValueError as err:
            raise ValueError("Error converting max_retries parameter: %s" % err)

        if max_retries > 0:
            http = requests.adapters.HTTPAdapter(max_retries=Retry(total=max_retries, backoff_factor=backoff_factor))
            https = requests.adapters.HTTPAdapter(max_retries=Retry(total=max_retries, backoff_factor=backoff_factor))
            logger.info('Session  max_retries using: %s' % max_retries)
            self.session.mount('http://', http)
            self.session.mount('https://', https)
        self.session.cookies = cookies

    def __get(self, url, params=None):
        response = self.session.get(url=url, params=params)
        logger.info('Resquest url: %s  Resquest params:%s'%(url,params))
        return response

    def _get(self, params_type, request_url, request_data):
        if params_type == "url":
            request_url = "%s%s" % (request_url, request_data)
            response = self.__get(url=request_url)
            return response
        elif params_type == "params":
            response = self.__get(url=request_url, params=request_data)
            return response

    def __post(self, url, data=None, json=None):
        response = self.session.post(url=url, data=data, json=json)
        return response

    def _post(self, params_type, request_url, request_data):
        """

        :param params_type:
        :param request_url:
        :param request_data:
        :return:
        """
        if params_type == "form":
            response = self.__post(url=request_url, data=json.dumps(eval(request_data)))
            return response
        elif params_type == 'json':
            response = self.__post(url=request_url, json=json.dumps(eval(request_data)))
            return response

    def request(self, request_method, request_url, params_type, request_data=None):
        """

        :param request_method:
        :param request_url:
        :param params_type:
        :param request_data:
        :return:
        """
        if request_method.lower() == "post":
            response = self._post(params_type, request_url, request_data, )
            return response
        elif request_method == "get":
            response = self._get(params_type, request_url, request_data)
            return response


if __name__ == '__main__':
    # r = requests.session()
    # result = r.get('http://www.tietonggroup.com/ttsd/publicNumber/login?key=dGlhbmhjLDExMTExMQ==')
    # print(type(json.loads(result.content)))
    # content = json.loads(result.content)
    # token = content['data']['token']
    # r = RequestsLibrary()
    r = HttpClient()
    res = r.request(request_method='get', request_url='https://www.baidu.com', params_type='params')
    print(res)
