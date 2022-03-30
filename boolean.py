true = lambda x: lambda y: x
false = lambda x: lambda y: y
tobool = lambda b: b(True)(False) # Convert Lambda boolean to python boolean
frombool = lambda x: true if x else false # convert python boolean to lambda boolean

IF = lambda condition, then, _else_: condition(then)(_else_)
NOT = lambda x: x(false)(true)
OR = lambda x,y: y(y)(x)
AND = lambda x,y: x(y)(x)
XOR = lambda x, y: x(NOT(y))(y)
COMP = lambda x,y: x(y)(NOT(y))