s='hello'
for i in range(4,1,-2):   ### range produces a list starting at 4 ending but not including 1 step -2
    print(s[i], end="")   ### range=[4,2] this is the list made, so s[4] is printed then s[2]
