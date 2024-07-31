def f(b):      ### this function takes an int as a parameter
    return a*b ### multiply a by b
a=4            ### because a is not defined in the function it looks for a outside which is defined here
print(f(4),a)  ### the print statement works because the function has an a before being called
### the answer is 16 4