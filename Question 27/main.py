def myFunction(theList):
    for row in theList:        ### the rows are the individual lists in the list
        for num in row:
            if num==0:
                continue       ### this skips to the next number the print does not get carried out
            print(num,end="")
        print()                ### By the end of a row this makes a new line for the next row