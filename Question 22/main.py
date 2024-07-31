def myfunction(d):
    lst=[] ### this is an empty list
    for thing in d:   ### thing represents a key in the dictionary
        if 'y' in d[thing]:  ### if one of the values of the key have the letter y
            lst.append(d[thing]) ### add the value to the lst
    return lst
d={'tree':'Oak', 'fish':'guppy','dog':'boxer','cat':'tabby'}
print(myfunction(d))
### answer is guppy tabby