#!/usr/bin/env python

import string
import re

steps = 16

def decipherChar(c):
    if c.istitle():
        return string.uppercase[(string.uppercase.index(c) - steps) % 26]
    else:
        return string.lowercase[(string.lowercase.index(c) - steps) % 26]

newfile = open('deciphered.txt','w')

with open('caesar.txt') as f:
    for line in f:
        newline = ''
        for c in line:
            if re.match('^[a-zA-Z]+$', c):
                newline += decipherChar(c)
            else:
                newline += c
        newfile.write(newline)

newfile.close()

# for output in cli
#with open('caesar.txt') as f:
#    for line in f:
#        newline = ''
#        for c in line:
#            if re.match('^[a-zA-Z]+$', c):
#                newline += decipherChar(c)
#            elif re.match('^\n+$', c):
#                continue
#            else:
#                newline += c
#        print newline



