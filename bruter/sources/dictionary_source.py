from source import WordsSources

class DictionarySource(WordsSources):
    """ :: Gets the words from a dictionary :: """

    def __init__(self, fileName):
        self.file_name = fileName
        self.file = open(fileName, "r")

    def __delattr__(self):
        if self.file.opened:
            self.file.close()

    def Next(self):
        """ :: Gets the next line of the opened file :: """