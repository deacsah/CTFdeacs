#!/usr/bin/env python
import urllib2
import os
import io

url = 'https://2013.picoctf.com/autoproblems/tmpnOIAxP.txt'
result = urllib2.urlopen(url).read(1000000)

with io.FileIO("caesar.txt", "w") as file:
    for line in result:
        file.write(line)




