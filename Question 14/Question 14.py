def f(b):    ### this function multiplies b by a
    global a ### this makes a variable a global(as in a is this value even outside the function)
    a=7
    return a*b
a=0          ### a is zero if the function is not called.
print(f(4),a) ### because the function is called, the global variable a runs and a will be equal to 7