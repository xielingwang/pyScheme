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

How to read these codes
-----
### builtin.py
This file includes the defines for ``list``, ``func`` and the operator for calculation or logic: ``+``,``-``,``>=``,``if``, ``and``,``or``, etc.

### expression.py
This file implement a Expression Class that contains the logic to evaluate a statement.

### parser.py
This file is easy to understand. It define a class analysis the words and build a tree for expression to evaluate.

### scope.py
This file define a class to implement the life cycles of variables.

That is all. Sorry for my poor english writings.

Some test code
-----
Now it ONLY supports such types: ``integer``, ``func``, ``list``, NO ``string`` and else. If you are interesting, you can try to add other type.
And I hasn't implement the COMMENT `; single line comment` or `# multiple lines comments #` yet. So if you try to execute the command follows, please DON'T copy the comment. 
Here are some test code and their expected results.
tuple[0] is the code, and tuple[1] is its expected output.

```lisp
>> (+ 1 2 3) ; add
6
>> (if 1 2 4) ; if 1 then 2 else 4
2
>> (if 0 2) ; if 0 then 2 else None
None
>> (def a 3) ; define a variable 'a'
3
>> a ; show the variable 'a'
3
>> (list 1  2  3  4) ; a list
(list 1 2 3 4)
>> (func (x) (+ x x) ; a function require an argument 'x'
(func (x) (+ x x))
>> (begin (def x 3) (* 1 2)) ; begin statement, it will return the result of the last statement
2
>> (def li (list 9 8 7 6)) ; define a variable 'li' of a list
(list 9 8 7 6)
>> (first li) ; first operation for list 'li'
9
>> (rest li) ; rest operation for list 'li'
(list 8 7 6)
>> (def sqr (func (x) (* x x))) ; define a function 'sqr' for square
(func (x) (* x x))
>> (sqr 5) ; execute function 'sqr' by 5
25
>> (def mul (func (x y) (* x y))) ; define a function 'mul' for mutiple
(func (x y) (* x y))
>> (def mul7 (mul 7)) ; define a partial function 'mul7' which require an argument and return a result equals the argument multiple by 7 
(func (x y) (* x y))
>> (mul7 9) ; try to execute the partial function 'mul7'
63
>> (> 3 2 1) ; 3 > 2 and 3 > 1
True
>> (> 2 2 1) ; 2 > 2 and 2 > 1
False
>> (= 3 3 3) ; 3 == 3 and 3 == 3
True
>> (= 3 3 2) ; 3 == 3 and 3 > 2
False
>> (and 1 2 3) ; 1 and 2 and 3
True
>> (and 1 2 (or 0 0 0 1)) ; 1 and 2 and (0 or 0 or 0 or 1)
True
>> ( begin 1 (and 9 8 7) (def gx 3) (sqr 9)) ; try a complex begin statement
81
>> (xor 1 1) ; 1 xor 1
False
>> (xor 0 0)
False
>> (xor 1 0)
True
>> (xor 0 1)
True
>> wtf ; call a undefined variable
error: 'wtf' is undefined.
>> (unfunc 1 2) ; call a undfined function
error: 'unfunc' is undefined.
```
