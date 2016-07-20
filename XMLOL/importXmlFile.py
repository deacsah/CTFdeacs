#!/usr/bin/env python
import urllib2
import os
import io

url = 'https://2013.picoctf.com/autoproblems/tmpPEdxZ7.xml'
result = urllib2.urlopen(url).read(1000000)

with io.FileIO("data.xml", "w") as file:
    for line in result:
        file.write(line)




