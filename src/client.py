import requests
import json
from utils.helpers import responseHelper
from base64 import b64encode

class Client():
    """
    Initializes a Client Object.
    """
    def __init__(self, config):
        self.apiKey = config["api_key"]
        self.username = config["username"]
        self.password = config["password"]

        if config["uri"] == "":
            self.baseUri = 'https://cloud.getconvoy.io/api/v1'
        else:
            self.baseUri = config["uri"]

        self.headers = {'Authorization': self.getAuthorization(), 'Content-Type': 'application/json; charset=utf-8'}

    def httpGet(self, path, query):
        try:
            response = requests.get(self.buildPath(path, query), headers=self.headers)
            return response.json(), response.status_code
        except BaseException as e:
            return responseHelper(e) 

    def httpPost(self, path, query, data):
        try:
            response = requests.post(self.buildPath(path, query), data=json.dumps(data), headers=self.headers)
            return response.json(), response.status_code
        except BaseException as e:
            return responseHelper(e) 

    def httpPut(self, path, query, data):
        try:
            response = requests.put(self.buildPath(path, query), data=json.dumps(data), headers=self.headers)
            return response.json(), response.status_code
        except BaseException as e:
            return responseHelper(e) 

    def httpDelete(self, path, query, data):
        try:
            response = requests.delete(self.buildPath(path, query), data=json.dumps(data), headers=self.headers)
            return response.json(), response.status_code
        except BaseException as e:
            return responseHelper(e) 

    def getBaseUrl(self):
        return self.baseUri

    def getAuthorization(self):
        if self.apiKey != "":
            return "Bearer %s" % self.apiKey

        return "Basic %s" % b64encode(("%s:%s" % (self.username, self.password)).encode('utf-8')).decode('utf-8')

    def buildPath(self, path, query):
        if self.hasQueryParameters(query):
            path = "%s%s?%s" % (self.baseUri, path, query)
            return path
        return "%s%s" % (self.baseUri, path)

    def hasQueryParameters(self, query):
        return len(query) > 0
