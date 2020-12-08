from bruter.sources.random_nums import RandomNumbersSource

class Bruter():
    """ Brute Forcing Class """

    def __init__(self, url, data, source, toDo):
        self.url = url
        self.data = data
        self.source = source
        self.toDo = toDo

    def start(self):
        while True:
            v = self.source.Next()
            if self.toDo(v):
                return True
        return False
    
