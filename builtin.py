#!/usr/bin/env python
# -*- coding: utf-8 -*-

#=================================================
# copyright Amin By [http://aminby.net]
# Since 2014-4
#=================================================

import math
from operator import mul
from scope import SScope
import types


# define Built-in List
class BIList(object):
    """docstring for BIList"""

    values = []

    def __init__(self, values):
        super(BIList, self).__init__()
        self.values = values
        
    def __str__(self):
        return "(list %s)" % (" ".join([str(x) for x in self.values]))

    def first(self):
        return self.values[0] if self.values else None

    def rest(self):
        return BIList(self.values[1:]) if self.values else BIList([])

# define built-in function
class BIFunction(object):
    """docstring for BIFunction"""

    body = None
    parameters = []
    scope = None

    def __init__(self, body, parameters, scope):
        super(BIFunction, self).__init__()
        self.body = body
        self.parameters = parameters
        self.scope = scope

    def __str__(self):
        return "(func (%s) %s)" % (" ".join(self.parameters), str(self.body))

    def computeFilledParams(self):
        return [x for x in [self.scope.findInTop(name) for name in self.parameters] if x]

    def isPartial(self):
        return len(self.computeFilledParams()) in range(2, len(self.parameters)-1)

    def evaluate(self):
        filledParams = self.computeFilledParams()
        if len(filledParams) < len(self.parameters):
            return self
        return self.body.evaluate(self.scope)

    def update(self, arguments):
        existedArguments = filter(None, [self.scope.findInTop(p) for p in self.parameters])
        newArguments = existedArguments + arguments
        newScope = self.scope.parent().spawnScopeWith(self.parameters, newArguments)
        return BIFunction(self.body, self.parameters, newScope)


# define built-in class
# 'member' is his interface method for external using
class BuiltIn(object):
    """docstring for BuiltIn"""

    # set
    @staticmethod
    def member(name, func=None):
        if not hasattr(BuiltIn,'functions'):
            BuiltIn.functions = {}
        if func is not None:
            BuiltIn.functions[name] = func
            return
        return BuiltIn.functions.get(name, None)

    @staticmethod
    def _sub(args, scope):
        args = [x.evaluate(scope) for x in args]
        return args[0] - math.fsum(args[1:])

    @staticmethod
    def _mul(args, scope):
        return reduce(mul, [x.evaluate(scope) for x in args])

    @staticmethod
    def _div(args, scope):
        args = [x.evaluate(scope) for x in args]
        dividend = reduce(mul, args[1:])

        if not dividend:
            raise Exception("dived is zero")
        return args[0] / dividend

    @staticmethod
    def _add(args, scope):
        return math.fsum([x.evaluate(scope) for x in args])

    @staticmethod
    def _sub(args, scope):
        if not args:
            raise Exception("'-' operator need arguments.")
        args = [x.evaluate(scope) for x in args]
        return args[0] - math.fsum(args[1:])

    @staticmethod
    def _mod(args, scope):
        if len(args) < 2:
            raise Exception("'%' operator need 2 arguments.")
        args = [x.evaluate(scope) for x in args[0:2]]
        return int(args[0]) % int(args[1])

    @staticmethod
    def _and(args, scope):
        for x in args:
            if not x.evaluate(scope):
                return False
        else:
            return True

    @staticmethod
    def _or(args, scope):
        for x in args:
            if x.evaluate(scope):
                return True
        else:
            return False

    @staticmethod
    def _xor(args, scope):
        return reduce(lambda x,y:x^y, [bool(x.evaluate(scope)) for x in args])

    @staticmethod
    def _not(args, scope):
        if not args:
            raise Exception("operator 'not' need 1 argument.")
        return not args[0].evaluate(scope)

    @staticmethod
    def _compare(op, args, scope):
        if len(args) < 2:
            raise Exception("compare operator need at least 2 arguments.")
        first = args[0].evaluate(scope)
        for x in args[1:]:
            if not eval("%f %s %f" % (first, op, x.evaluate(scope))):
                return False
        else:
            return True

    @staticmethod
    def _if(args, scope):
        len_a = len(args)
        if len_a < 2:
            raise Exception("if need at least arguments.")
        if args[0].evaluate(scope):
            return args[1].evaluate(scope)
        elif len_a > 2:
            return args[2].evaluate(scope)
        return None

    @staticmethod
    def _def(args, scope):
        return scope.define(args[0].value, args[1].evaluate(SScope(scope)))

    @staticmethod
    def _begin(args, scope):
        if not args:
            return None
        return [x.evaluate(scope) for x in args][-1]

    @staticmethod
    def _func(args, scope):
        if len(args) < 2:
            raise Exception("'func' operator need 2 arguments.")
        return BIFunction(args[1], [x.value for x in args[0].children], SScope(scope))


#===============================================
# define the built-in operators and functions
#===============================================
# keywords
BuiltIn.member("func", BuiltIn._func)
BuiltIn.member("def", BuiltIn._def)
BuiltIn.member("begin", BuiltIn._begin)
BuiltIn.member("if", BuiltIn._if)

# basic calculator
BuiltIn.member("+", BuiltIn._add)
BuiltIn.member("-", BuiltIn._sub)
BuiltIn.member("*", BuiltIn._mul)
BuiltIn.member("/", BuiltIn._div)
BuiltIn.member("%", BuiltIn._mod)

# compare
BuiltIn.member("=", lambda args, scope: BuiltIn._compare("==", args, scope))
BuiltIn.member(">", lambda args, scope: BuiltIn._compare(">", args, scope))
BuiltIn.member("<", lambda args, scope: BuiltIn._compare("<", args, scope))
BuiltIn.member("<=", lambda args, scope: BuiltIn._compare("<=", args, scope))
BuiltIn.member(">=", lambda args, scope: BuiltIn._compare(">=", args, scope))

# logic
BuiltIn.member("and", BuiltIn._and)
BuiltIn.member("or", BuiltIn._or)
BuiltIn.member("xor", BuiltIn._xor)

# list
BuiltIn.member("list", lambda args, scope: BIList([x.evaluate(scope) for x in args]))
BuiltIn.member("first", lambda args, scope: args[0].evaluate(scope).first())
BuiltIn.member("rest", lambda args, scope: args[0].evaluate(scope).rest())
#todo BuiltIn.member("append")
#todo BuiltIn.member("empty?")