from boolean import true, false

#Lambda Numerals

zero = lambda f: lambda x: x # <= the lambda numeral "0"
increment = lambda n: lambda f: lambda x: f(n(f)(x)) # <= returns the lambda numeral n+1
decrement = lambda n: lambda f: lambda x: n(lambda g: lambda h: h(g(f)))(lambda u: x)(lambda u: u) # <= takes a lambda numeral as an argument and returns the previous lambda numeral ( ie decrement(two) == one)
fromint = lambda n: zero if n < 1 else increment(numeral(n-1)) # <= takes a Python Integer and reurns the equvilent Lambda numeral
toint = lambda n: n(lambda x: x+1)(0) # <= converts a Lambda numeral to Python Integers

# Math Functions

add = lambda m, n: m(increment)(n) # returns the sum of two numerals
subtract = lambda m, n: n(decrement)(m) # returns the difference of two numerals
multiply = lambda m, n: m(lambda x: add(n,x))(zero)
exponent = lambda m, n: n(lambda x: multiply(m,x))(increment(zero))
square = lambda n: exponent(n,increment(increment(zero)))

# Predicates

iszero = lambda n: n(lambda x: false)(true)
_lessthanorequal = lambda m, n: iszero(subtract(n,m))
leq = _lessthanorequal