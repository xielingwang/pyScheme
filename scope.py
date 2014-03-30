#!/usr/bin/env python
# -*- coding: utf-8 -*-

#=================================================
# copyright Amin By [http://aminby.net]
# Since 2014-4
#=================================================

class SScope(object):
    """docstring for SScope"""

    __parent = None
    __varsTable = {}

    def __init__(self, parent = None):
        super(SScope, self).__init__()
        self.__parent = parent
        self.__varsTable = {}

    def parent(self):
        return self.__parent

    def __str__(self):
        ret = ",".join(self.__varsTable.keys())
        if self.__parent:
            ret += " <= %s" % str(self.__parent)
        return ret

    def find(self, name):
        curScope = self
        while curScope:
            if name in curScope.__varsTable.keys():
                return curScope.__varsTable[name]
            curScope = curScope.__parent
        if name in SScope.constant():
            return SScope.constant(name)
        raise Exception("'%s' is undefined." % name)

    def define(self, name, value):
        self.__varsTable[name] = value
        return self.__varsTable[name]

    def spawnScopeWith(self, names, values):
        if len(names) < len(values):
            raise Exception("too many arguments.")
        scope = SScope(self)
        for index,value in enumerate(values):
            scope.__varsTable[names[index]] = value
        return scope

    def findInTop(self, name):
        if self.__varsTable.has_key(name):
            return self.__varsTable[name]
        return

    @staticmethod
    def constant(name=None, value=None):
        if not hasattr(SScope, '_constants'):
            SScope._constants = {}
        if name is None:
            return SScope._constants
        if value is not None:
            SScope._constants[name] = value
        return SScope._constants.get(name, None)


SScope.constant('pi', 3.1415916)
SScope.constant('e', 2.718281828)


if '__main__' == __name__:
    a = SScope()
    a.define('a1', '3')
    a.define('a2', '4')
    print a
    b = SScope(a)
    b.define('b1', '3')
    b.define('b2', '3')
    print b
    c = SScope(b)
    c.define('c1', '5')
    print c