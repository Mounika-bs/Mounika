#L = ["Geeks\n", "for\n", "Geeks\n"] 
file1 = open('myfile.txt', 'w') 
file1.writelines(L) 
file1.close() 
file1 = open('myfile.txt', 'r') 
Lines = file1.readlines() 
count = 0
for line in Lines: 
    print("Line{}: {}".format(count, line.strip()))
