# program to count no of lines in a text file
fname = input('Enter a file name: ')
f=open(fname)
c=0
t=f.read()
tlist=t.split("\n")
for i in tlist:
    if i:
        c+=1
print("the no of lines in the required text file is:",c)