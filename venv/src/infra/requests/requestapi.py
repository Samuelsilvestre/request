import requests
from requests import Request
from typing import Type

class RequestApi:
    
    ''''request api'''

    def __init__(self, url: str, page: int=None):
        self.get = self.__get(url, page)

    def __get(self, url: str, page: int):
        request_body = requests.Request(
            method = 'GET',
            url = url,
            params = {'page': page}
        )
        request_prepare = request_body.prepare()
        response = self.__send_http(request_prepare)
        return  response   
    
    @classmethod
    def __send_http(cls, request_prepare: Type[Request]):
        session_http = requests.session()
        send = session_http.send(request_prepare)
        return send
 