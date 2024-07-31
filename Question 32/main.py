def myFunction(filename):
    infile=open(filename)  #opens file and needed first to edit/read it
    lst=infile.read()      # reads the text and has the text as its value
    infile.close()         # closes the file
    newLst=lst.split()     # splits the lst into a list of words
    return len(newLst)
print(myFunction("pizza.txt"))
### this returns the number of words  in the file
### pizza.txt is here as an example
