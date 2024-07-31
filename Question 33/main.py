def myFunction(filename):
    infile=open(filename)      ### open the file
    content=infile.readlines() ### makes a list where each element is a line
    infile.close()
    return len(content)        ### returns the length of the list aka the number of lines
print(myFunction("Lines.txt"))