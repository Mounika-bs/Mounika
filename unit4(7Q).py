# program to read a file line by line and store it into an array
def f_read(fname):
    ar=[]
    with open(fname) as f:
        for line in f:
            ar.append(line)
        print(ar)
fname = input('Enter a file name: ')
f_read(fname)