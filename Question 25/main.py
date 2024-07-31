def myfunction(d):
    d2={'Twain':'Mark'}
    d.update(d2)        ### update dictionary d with d2 by adding the elements from d2
    return d2
d={1:"for the money","two":"for the show"}
print(myfunction(d))
### this will just return d2 unaltered since d was the one altered