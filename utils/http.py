import requests

class HttpManager():
    """ Manages HTTP resquests """

    def make_request(self, url, data = None):
        """ Invokes an HTTP GET request """
        return requests.get(url).text
