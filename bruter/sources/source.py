class WordsSources():
    """ Words Source Base Class """

    def __init__(self, length, prefix = 0, suffix = 0):   
        self.length = length
        self.prefix = prefix
        self.suffix = suffix

    def Next(self):
        """ :: Virtual Next Method :: """
        return None