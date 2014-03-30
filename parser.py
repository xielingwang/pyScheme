#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import re
from expression import SExpression

class SParser(object):
    """docstring for SParser"""

    def __init__(self):
        super(SParser, self).__init__()

    def tokenize(self, code):
        lexes = re.split('[ \r\n\t]+', code.replace('(', ' ( ').replace(')', ' ) '))
        return [elem for elem in lexes if elem]

    def parseAsIScheme(self, code):
        program = SExpression()
        current = program
        for lex in self.tokenize(code):
            if lex == '(':
                newNode = SExpression(value=lex, parent=current)
                current.children.append(newNode)
                current = newNode
            elif lex == ')':
                current = current.parent
            else:
                current.children.append(SExpression(value=lex, parent=current))

        return program.children[0] if program.children else None


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    psr = SParser()

    test_statements = (
        ("(if 1 2 4)", 2),
        ("(if 0 2)", None),
        ("(def a 3)", 3),
        ("a", 3),
        ("(list 1  2  3  4)", "(list 1 2 3 4)"),
        ("(func (x) (+ x x)", "(func (x) (+ x x))"),
        ("(begin (def x 3) (* 1 2))", 2),
        ("(def li (list 9 8 7 6))", "(list 9 8 7 6)"),
        ("(first li)", 9),
        ("(rest li)", "(list 8 7 6)"),
        ("(def mi (func (x) (* x x)))", "(func (x) (* x x))"),
        ("(mi 5)", 25),
        ("(def mul (func (x y) (* x y)))", "(func (x y) (* x y))"),
        ("(def mul7 (mul 7))", "(func (x y) (* x y))"),
        ("(mul7 9)", 63),
        ("(> 3 2 1)", True),
        ("(> 2 2 1)", False),
        ("(= 3 3 3)", True),
        ("(= 3 3 2)", False),
        ("(and 1 2 3)", True),
        ("(and 1 2 (or 0 0 0 1))", True),
        ("( begin 1    (and 9 8 7) (def gx 3) (mi 9))", 81),
        ("(xor 1 1)", False),
        ("(xor 0 0)", False),
        ("(xor 1 0)", True),
        ("(xor 0 1)", True),
        ("wtf", "error: 'wtf' is undefined."),
        ("(unfunc 1 2)", "error: 'unfunc' is undefined.")
        )

    for s,r in test_statements:
        print "tokenize: %s => " % s,psr.tokenize(s)
    print

    for s,r in test_statements:
        print "parseAsIScheme: %s => " % s,psr.parseAsIScheme(s)
    print

    for s,r in test_statements:
        rr = psr.parseAsIScheme(s).evaluate_excepted()
        print "evaluate_excepted",str(r) == str(rr),":", s, "=>", rr
        # print "'%s' '%s'" % (str(r), str(rr))
