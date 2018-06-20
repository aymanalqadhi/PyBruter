from source import WordsSources

class RandomStringsSource(WordsSources):
    """ :: Generates random strings :: """



    def __init__(self, length, prefix = 0, suffix = 0):   
        WordsSources.__init__(self, length, prefix, suffix)

    def Next(self, exclude = []):
        """ :: Generates a new string without characters from exclude :: """

        ret = ''
        return ret