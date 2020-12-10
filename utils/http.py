import requests

class HttpManager():
    """ Manages HTTP resquests """

    def make_request(self, url, data = None):
        """ Invokes an HTTP GET request """
        resp = requests.get(url)
        ret = resp.text
        resp.close()

        return ret
