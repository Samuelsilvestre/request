from typing import Type
from src.infra.requests.requestapi import *

class MakeRequestAPI:

    @staticmethod
    def get_json(url: str, page: int=None) -> Type[RequestApi]:
        if url:
            try:
                request_api = RequestApi(url, page)
                json = request_api.get.json()
                
                return json
            
            except:
                return {"status": request_api.get.status_code}

        return {"erro": "falha na operação"}    
                
            
