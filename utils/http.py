import urllib

class HttpManager():
    """ Manages HTTP resquests """

    def make_request(self, url, data = None):
        """ Invokes an HTTP GET request """

        req = urllib.urlopen(url, data)
        ret = req.read()
        req.close()

        return ret