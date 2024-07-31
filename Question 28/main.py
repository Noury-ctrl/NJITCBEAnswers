def myFunction(aNumList):
    result=0
    for i in aNumList:     ### for the elements in the list
        if i%2==0:         ### if the remainder from i/2 is 0
            result+=1      ### add 1 to the result
    return result
numList=[4,0,1,-2]
print(myFunction(numList)) ### this will return 3 cause 4,0,-2 are divisible by 2