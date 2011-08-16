#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, os

if not sys.argv[1] :
    print 'missing param'
    sys.exit(-1)

filepath = os.path.abspath(sys.argv[1])

if not os.path.exists(filepath) :
    print 'file does not exist: ', filepath
    sys.exit(-2)

f = open(filepath, 'r')

for line in f:
    print '<a href="http://' + line.strip() + '">' + line.strip() + '</a><br />'

f.close();