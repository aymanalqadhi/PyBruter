from source import WordsSources
from math import floor, log10, pow
from random import randint

class RandomNumbersSource(WordsSources):
    """ Source to generate random numbers """

    def __init__(self, length, prefix = 0, suffix = 0):   
        WordsSources.__init__(self, length, prefix, suffix)

    def Next(self):
        """ :: Gets the next random number :: """

        ret = 0
        minLen = self.length 

        if  self.prefix > 0:
            pLen = floor(log10(self.prefix)) + 1
            minLen += pLen
            ret = self.prefix * pow(10, self.length)

        if  self.suffix > 0:
            minLen += floor(log10(self.suffix))

        ret += randint(pow(10, self.length - 1), pow(10, self.length) - 1)
        return int(ret)