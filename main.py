from argparse import ArgumentParser
from bruter.sources.random_nums import RandomNumbersSource
from net.http import HttpManager
from time import sleep, time, strftime, localtime
from termcolor import colored
from sys import stdout

parser = ArgumentParser()
parser.parse_args()

print '\n\t--<( Attack Started on: %s )>--\n' % colored(strftime("%H:%M:%S"), 'yellow', attrs=['bold'])
print ' * Url: %s' % colored('http://a.com/login', 'cyan', attrs=['bold'])
print ' * Query: %s' % colored('username=?&password=123', 'cyan', attrs=['bold'])
print ' * Attack Method: %s' % colored('Bruteforce (Random Numbers)', 'cyan', attrs=['bold'])

print 

src = RandomNumbersSource(6, 29)
start_time = time()
tries = 0

while True:
    v = src.Next()
    tries += 1

    stdout.write('\r\t Current Entry [ %s ] Try #%d, %s Elapsed' % (colored(str(v), 'cyan', attrs=['bold']), tries, colored('%ds' % (time() - start_time), 'yellow')))
    stdout.flush()

    if(str(v).startswith('2999')):
        print '\n\n\t   ' + '-' * 40
        print '\n\t\t   --<( %s )>--' % colored('Match Found!', 'yellow', attrs=['bold'])
        print '\n\t\t     * Value: %s' % colored(str(v), 'cyan', attrs=['bold'])
        print '\t\t     * Total Tries: %s\n' % colored(str(tries), 'yellow', attrs=['bold'])
        break

    sleep(0.01)
    
