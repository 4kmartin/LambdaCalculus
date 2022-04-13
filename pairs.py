from boolean import true, false
from numerals import zero, increment

PAIR = lambda x, y: lambda f: f(x)(y) # a pair is a tuple of two elements

CAR = lambda p: p(true) # return the first element or Contents of the "A" Register
CDR = lambda p: p(false) # return the last element or Contents of the "D" Register
REASSIGN = lambda p, new, fe: fe(PAIR(new,CDR(p)))(PAIR(CAR(p),new))

toTuple = lambda p: (CAR(p),CDR(p))

NIL = true
NULL = lambda p: p(lambda x: lambda y: false) # checks if a pair is empty