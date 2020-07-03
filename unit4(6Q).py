# program to read a file line by line and store it into a list
def f_read(fname):
    with open(fname) as f:
        flist=f.readlines()
        print(flist)
fname = input('Enter a file name: ')
f_read(fname)