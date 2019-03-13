#!/usr/bin/python2.7

import sys

name = sys.argv[1]
age = int(sys.argv[2])
diff = 100 - age

print 'Hello', name + ', you will be 100 in', diff, 'years!'


#just use it like a shell scrpit in terminal:  test.py Jack 24
