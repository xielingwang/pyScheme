#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scope import SScope
from builtin import BuiltIn

def numberic(strValue):
    val = None
    try:
        val = int(strValue)
        val = int(strValue)
    except ValueError:
        if val:
            return val
    return val

class SExpression(object):
    """docstring for SExpression"""

    value = ''
    parent = None
    children = []

    def __init__(self, value='', parent=None):
        super(SExpression, self).__init__()
        self.value = value
        self.parent = parent
        self.children = []

    def __str__(self):
        if self.value == '(':
            return '(' + ' '.join([str(elem) for elem in self.children]) + ')'
        else:
            return self.value

    def evaluate_excepted(self, scope=SScope()):
        try:
            return self.evaluate(scope)
        except Exception, e:
            return "error: %s" % e

    def evaluate(self, scope=SScope()):
        while True:
            # a variable or a constant
            # that hasn't children
            if not self.children:
                num = numberic(self.value)
                if num is not None:
                    return num
                return scope.find(self.value)

            fchild = self.children[0]

            # it's a built-in function
            func_built_in = BuiltIn.member(fchild.value)
            if func_built_in is not None:
                return func_built_in(self.children[1:], scope)

            # evaluate the function
            func = fchild.evaluate(SScope(scope)) if fchild.value == '(' else scope.find(fchild.value)
            arguments = [expr.evaluate(scope) for expr in self.children[1:]]
            newFunc = func.update(arguments)

            if not newFunc.isPartial():
                # if is a partial function
                """
                (def mul (func (x y) (* x y)))
                (def mul5 (mul 5))
                (mul5 7) => 35
                """
                return newFunc.evaluate()
            else:
                self = newFunc.body
                scope = newFunc.scope


if __name__ == '__main__':
    for x in ["123", "124.1", "124m"]:
        print "%s = %s" % (x, numberic(x))
    se = SExpression(value='(')
    se.children.append(SExpression(value='+'))
    se.children.append(SExpression(value='3'))
    se.children.append(SExpression(value='5'))
    print se
    print se.evaluate()