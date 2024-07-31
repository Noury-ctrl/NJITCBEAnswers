def readAge(filename):
    strAge=None
    while True:
          try:
            if strAge is None:   #### in order for the method to carry out strAge has to be none
               infile=open(filename)
               strAge=infile.readline() ### reads one line which is your age
               age=int(strAge)  ### variable has to be age in order for the print statement to work
               print('Next year you will be',age+1)
               break
          except ValueError:
                 print('Value cannot be converted to integer')
                 strAge=input("Enter a proper age: ")

          except FileNotFoundError:
                 print('input file is missing:'"'"+filename+"'")
                 filename=input("Enter a new filename: ")
readAge('age.txt') ### example