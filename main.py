#!/usr/bin/env python
# -*- coding: utf-8 -*-

#=================================================
# copyright Amin By [http://aminby.net]
# Since 2014-4
#=================================================

from parser import SParser

PRT_FAIL = '\033[91m'
OKBLUE = '\033[94m'
PRT_ENDC = '\033[0m'

def greeting():
    print OKBLUE + "Welcome to use pyScheme, it's just a simple project for learning how an interpreter works."
    print "I'm Amin By, from China. Here's my homepage: http://aminby.net"
    print PRT_ENDC


def helping():
    print "the messages for help, it may be a long text."


def goodbye():
    print OKBLUE + "Thank you for using pyScheme. Bye!", PRT_ENDC
    print


if __name__ == '__main__':
    greeting()

    psr = SParser()
    while True:
        code = raw_input("pySchm> ").strip()
        if code in ('help', 'documents'):
            helping()
            continue

        if code in ('exit', 'quit'):
            goodbye()
            break

        # get expression and evaluate it
        expr = psr.parseAsIScheme(code)
        try:
            if expr:
                print 'pySchm>', expr.evaluate()
        except Exception, e:
            print PRT_FAIL + 'pySchm>', 'error: %s' % e, PRT_ENDC

