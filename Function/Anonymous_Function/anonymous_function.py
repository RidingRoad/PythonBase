"""anonymous function:   lambda  [arg1[, arg2, ... argN]]:expression
    :return callable function object"""

"""normal expression format"""
def re_True():
    return  True

"""anonymous function format"""

a = lambda : True   # it is the same effect to the above.

# we can use a variant to save the anonymous function so that we can use(call)


print(re_True())
print(a())



