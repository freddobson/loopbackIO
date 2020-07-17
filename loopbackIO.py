import requests
import json
import logging

class Api:
    def __init__(self, url, token, headers=None):
        self.url = url
        self.token = token
        if headers not None:
            if isinstance(headers,dict):
                self.header = headers
                self.header['Authorization'] = token
            self.header = {'Authorization': token}

class Filter:			logging.error("Supply a valid Api object.")
            else:
                logging.warning('"headers" must be of type "dict". Skipping')
                self.header = {'Authorization': token}
        else:
			raise Exception('ApiError')
		self.object_type = object_type
		self.api = api

        self.where = where # dict
    def __init__(self, where=None, order=None, fields=None, include=None:
        self.order = order
		
        self.fields = fields        self.include = include


		if not isinstance(filter, Filter):
class Request:
	def __init__(self, object_type, api):
		if not isinstance(api, Api)
	def get(self, filter, unlimited=False):
			logging.error("filter parameter must be instance of Filter class.")
			raise Exception('FilterError')
		request_url = self.api.url + '/api/' + self.object_type + '?filter='			try:

		payload = dict()			payload['where'] = filter.where
		while True:

		payload['skip'], payload['limit'] = 0, 1000
				response = requests.get(request_url + json.dumps(payload), headers=self.api.header)
		if filter.where is not None:
			except:
				logging.error("The error is {0}",format(err))
				raise Exception("RequestError")
			if response.status_code != 200:
                logging.error(str(response.status_code) + " " + response.reason + ": " + response.json()['error']['message']
                raise Exception("httpError")
            else:
                logging.info('Successful request: " + request.utils.unquote(response.request.url))
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
			
		