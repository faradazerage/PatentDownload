#!/usr/bin/python
import sys
import re
import urllib2
import os

if not os.path.exists('patents'):
    os.makedir('patents')

with open(sys.argv[1]) as fp:
    os.chdir('patents')
    for line in fp:
        lines = line.split(" ")
        if re.match(r'^\d{11}$', lines[1]):
            name = lines[1][9:11] + '/' + lines[1][0:4] + '/' + lines[1][7:9] + '/' + lines[1][4:7]
            addr = 'http://pimg-faiw.uspto.gov/fdd/' + name + '/0.pdf'
            patent = urllib2.urlopen(addr)
            with open(lines[1] + '.pdf', 'wb') as output:
                output.write(patent.read())
        if re.match(r'^\d{7}$', lines[1]):
            name = lines[1][5:7] + '/' + lines[1][2:5] + '/0' + lines[1][0:2]
            addr = 'http://pimg-fpiw.uspto.gov/fdd/' + name + '/0.pdf'
            patent = urllib2.urlopen(addr)
            with open(lines[1] + '.pdf', 'wb') as output:
                output.write(patent.read())
