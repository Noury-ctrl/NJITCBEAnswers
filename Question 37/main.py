def myFunction(aStr):
    result=len(aStr.split(' ')) # len() is length  .split splits up words into a list based on spaces
    return result
exclamation="As easy as 123"
print(myFunction(exclamation))