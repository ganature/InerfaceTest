# coding=utf-8
import requests
import json

class RequestsLibrary(object):
    """
    封装Requests库
    """
    def __init__(self):
        self.session=requests.session()
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



if __name__=='__main__':
    r=requests.session()
    result=r.get('http://www.tietonggroup.com/ttsd/publicNumber/login?key=dGlhbmhjLDExMTExMQ==')
    print type(json.loads(result.content))
    content=json.loads(result.content)
    token=content['data']['token']
    r=RequestsLibrary()
    r.get_name()
