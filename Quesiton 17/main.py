def readAge(filename):
    infile=open(filename)     ### this could throw a FileNotFoundError
    strAge=infile.readline()  ### this is more dependent on line 2
    age=int(strAge)      ### year is not defined NameError
    return 'born in{}'.format(age)