#!/usr/bin/python2.7

import sys
import optparse

parser = optparse.OptionParser()
parser.add_option('-n', '--name', dest='name', help='Your Name')
parser.add_option('-a', '--age', dest='age', help='Your Age', type=int)

(options, args) = parser.parse_args()

if options.name is None:
    options.name = raw_input('Enter Name:')

if options.age is None:
    options.age = int(raw_input('Enter Age:'))

sayHello = 'Hello ' + options.name + ','

if options.age == 100:
    sayAge = 'You are already 100 years old!'
elif options.age < 100:
    sayAge = 'You will be 100 in ' + str(100 - options.age) + ' years!'
else:
    sayAge = 'You turned 100 ' + str(options.age - 100) + ' years ago!'

'''
usage: test2.py [options]

options:
  -h, --help            show this help message and exit
  -n NAME, --name=NAME  Your Name
  -a AGE, --age=AGE     Your Age
'''
