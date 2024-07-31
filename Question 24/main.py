def frequency(thelist):
    counters={}                      ### empty dictionary
    for item in thelist:
        if item not in  counters:    ### the if statement is for adding new unique grades not in the counter
            counters[item]=1
        else:
            counters[item]+=1
    return counters                  ### returns the dictionary
### not in
### item
### item
