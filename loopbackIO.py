import requests
import json
import logging

class Api:
    def __init__(self, url, token, headers=None):
        self.url = url
        self.token = token
        if headers is not None:
            if isinstance(headers,dict):
                self.header = headers
                self.header['Authorization'] = token            
            else:
                logging.warning('"headers" must be of type "dict". Skipping')
                self.header = {'Authorization': token}
        else:
            self.header = {'Authorization': token}




class Filter:        
    def __init__(self, where=None, order=None, fields=None, include=None):
        self.order = order
        self.where = where # dict        
        self.fields = fields        
        self.include = include


      
class Request:
    def __init__(self, object_type, api):
        if not isinstance(api, Api):
            raise Exception('ApiError')
            logging.error("Supply a valid Api object.")
        else:
            self.object_type = object_type
            self.api = api        
    def get(self, filter, unlimited=False):
        if not isinstance(filter, Filter):
            logging.error("filter parameter must be instance of Filter class.")
            raise Exception('FilterError')  
        request_url = self.api.url + '/api/' + self.object_type + '?filter='            

        payload = dict()            
        if filter.where is not None:
            payload['where'] = filter.where
		
        while True:

            payload['skip'], payload['limit'] = 0, 1000
            try:
                response = requests.get(request_url + json.dumps(payload), headers=self.api.header)    
            except:
                logging.error("The error is {0}",format(err))
                raise Exception("RequestError")
            if response.status_code != 200:
                logging.error(str(response.status_code) + " " + response.reason + ": " + response.json()['error']['message'])
                raise Exception("httpError")
            else:
                logging.info('Successful request: ' + requests.utils.unquote(response.request.url))
            if (payload['skip'] == 0):
                response = response.json()
                if not unlimited:
                    break
            else:
                if (len(response.json()) > 0):
                    response.extend(response.json())
                else:
                    break
            payload['skip'] += 1000
        return response
            
        