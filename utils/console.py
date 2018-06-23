from sys import stdout
from time import sleep

def backspace(n):
    stdout.write('\b' * n)

i = 0
stdout.write("Testing: %3d" % i)
stdout.flush()

while i < 10000:
    i += 1
    backspace(5)
    stdout.write(" %4d" % i)
    stdout.flush()
    sleep(0.001)