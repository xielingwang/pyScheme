==============================
PyScheme, a scheme for pythonistas
==============================

It is a small scheme written in Python. Its goals are not to implement any specific lisp dialect, but to explain how to implement an ``interpretor``. 
There is a [my blog](http://aminby.net/2014/03/easy-way-build-code-interpreter/) to explain how these codes been produced.


Required
-----
The program build and test in python 2.7.6. DID NOT support Python 3 yet.

How to play
-----
Download or git out them, then run ```python main.py```. It's an interact command line. Play the simple ``Scheme`` script. Enjoy it.

Also, you can run
```shell
python scope.py
python parser.py
python expression.py
```
and see the test results for each module.

How to read these code
-----
``builtin.py`` includes the defines for ``list``, ``func`` and the operator for calculation or logic: ``+``,``-``,``>=``,``if``, ``and``,``or``, etc.

``expression.py`` implement the logic to evaluate an expression.

``parser.py`` is easy to understand. analysis the words and build a tree for expression to evaluate.

``scope.py`` is a class to implement the life cycle of the variables.

That is all. Sorry for my poor english writings.

Some test code
-----
Now it ONLY supports such types: ``integer``, ``func``, ``list``, NO ``string`` and else. If you are interesting, you can try to add other type.
Here are some test code and their expected results.
tuple[0] is the code, and tuple[1] is its expected output.

```lisp
statements = (
  ("(+ 1 2 3)", 6),
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
```
