def myFunction(d):
    if 2 in d:        ### if the int 2 is part of the dictionary as a key
        return d[2]   ### return the values that correspond to the key 2
    else:
        return 2 in d ### this will return False cause else only occurs if "2 in d" is false
d={1:"for the money", "two":"for the money"}
print(myFunction(d))