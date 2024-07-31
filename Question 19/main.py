def readAge(filename):
    try:
        infile=open(filename) ### you are trying to open the file that you are plugging into the function
        age=int(strAge)
    except ValueError:         ### filename would have a FilenotFoundError the int method has ValueError
        print("Value cannot be converted into an integer") ### keyword Value
    except FileNotFoundError:
        print('input file is missing:', "'"+filename+"'") ### filename is what the error is referring to