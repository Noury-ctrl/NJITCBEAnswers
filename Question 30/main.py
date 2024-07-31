def myFunction(aStr):
    result= len(aStr.split('y'))  ### len() returns the length of the parameter placed
    return result                 ###.split() splits up words in a string into lists
exclamation="As easy as 123"      ### if blank, .split() splits up based on whitespaces.
print(myFunction(exclamation))    ### because y is there the split will split along the lines of the letter y
                                  ### for exclamation its "As eas" split cause of y in easy  " as 123"
                                  ### resulting in a list["As eas", " as 123"] which is length 2
                                  ### answer is 2