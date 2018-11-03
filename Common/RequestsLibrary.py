# coding=utf-8
import requests
import json
import logging


class RequestsLibrary(object):
    """
    封装Requests库
    """

    def __init__(self):
        pass


class HttpClient(object):
    def __init__(self):
        pass

    @staticmethod
    def __post(url, data=None, json=None, **kargs):
        response = requests.post(url=url, data=data, json=json)
        return response

    @staticmethod
    def __get(url, params=None, **kargs):
        response = requests.get(url=url, params=params)
        return response

    def _get(self,params_type,request_url,request_data,headers,cookies):
        if params_type == "url":
            request_url = "%s%s" % (request_url, request_data)
            response = self.__get(url=request_url, headers=headers, cookies=cookies)
            return response
        elif params_type == "params":
            response = self.__get(url=request_url, params=request_data, headers=headers, cookies=cookies)
            return response
    def request(self,
                request_method,
                request_url,
                params_type,
                request_data=None,
                headers=None,
                cookies=None):

        if request_method.lower() == "post":
            if params_type == "form":
                response = self.__post(url=request_url, data=json.dumps(eval(request_data)), headers=headers,
                                       cookies=cookies)
                return response
            elif params_type == 'json':
                response = self.__post(url=request_url, json=json.dumps(eval(request_data)), headers=headers,
                                       cookies=cookies)
                return response
        elif request_method == "get":
            if params_type == "url":
                request_url = "%s%s" % (request_url, request_data)
                response = self.__get(url=request_url, headers=headers, cookies=cookies)
                return response
            elif params_type == "params":
                response = self.__get(url=request_url, params=request_data, headers=headers, cookies=cookies)
                return response


if __name__ == '__main__':
    # r = requests.session()
    # result = r.get('http://www.tietonggroup.com/ttsd/publicNumber/login?key=dGlhbmhjLDExMTExMQ==')
    # print(type(json.loads(result.content)))
    # content = json.loads(result.content)
    # token = content['data']['token']
    # r = RequestsLibrary()
    r=HttpClient()
    res=r.request(request_method='get',request_url='http://www.baidu.com',params_type='params')
    print(res)
