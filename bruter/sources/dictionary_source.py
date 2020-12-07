from bruter.sources.source import WordsSources

class DictionarySource(WordsSources):
    """ :: Gets the words from a dictionary :: """

    def __init__(self, fileName):
        self.file_name = fileName
        self.file = open(fileName, "r")

    def __exit__(self, ex_type, ex_code, traceback):
        if self.file.opened:
            self.file.close

    def Next(self):
        """ :: Gets the next line of the opened file :: """
        line = self.file.readline(-1)
        if line == '':
            return None
        return line[:-1]
