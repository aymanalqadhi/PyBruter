from utils.http import HttpManager

import argparse
import re

def valid_url(s, pat = re.compile(r'^((http|https|ftp)\://)([a-zA-Z0-9\.\-]+(\:[a-zA-Z0-9\.&amp;%\$\-]+)*@)*((25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9])\.(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9]|0)\.(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9]|0)\.(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[0-9])|localhost|([a-zA-Z0-9\-]+\.)*[a-zA-Z0-9\-]+\.(com|edu|gov|int|mil|net|org|biz|arpa|info|name|pro|aero|coop|museum|[a-zA-Z]{2}))(\:[0-9]+)*(/($|[a-zA-Z0-9\.\,\?\'\\\+&amp;%\$#\=~_\-]+))*$')):
    if not pat.match(s):
        raise argparse.ArgumentTypeError
    return s

parser = argparse.ArgumentParser(description='Starts an http/https attack using bruteforce/dictionary-based methods.')

parser.add_argument('url', help='url to start attack on', type=valid_url)
parser.add_argument('-d', '--data', help='The data to try on, ? for the unknown parameter')
parser.add_argument('--delay', help='The data to try on, ? for the unknown parameter', default=0, type=int)
parser.add_argument('-f', '--fpattern', help='A Pattern to check each response on and continue if it matches', default='var error')
parser.add_argument('-s', '--spattern', help='A Pattern to check each response on and continue if it does not matches', default='')

parser.add_argument('--post', help='Use HTTP POST requests')
parser.add_argument('--get', help='Use HTTP GET requests')

parser.add_argument('--prefix', help='A suffix to add after the parameter value', default='')
parser.add_argument('--suffix', help='A prefix to add before the parameter value', default='')
parser.add_argument('--length', type=int, help='The length of the randomly generated value', default=6)

args = parser.parse_args()

url = args.url
if str(url).endswith('/'):
    url = url[:-1]

delay = args.delay
data = args.data

if not data:
    data  = 'username=?'
elif str(data).find('?') == -1:
    if str(data).endswith('?'):
        data += '&'
    data += 'username=?'


fpatt = re.template(args.fpattern)
spatt = re.template(args.spattern)

http = HttpManager()
