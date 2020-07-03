# f=open("filename1.txt","w")
f.write("line number is 1\n")
f.write("line number is 2\n")
f.write("line number is 3\n")
f.write("line number is 4\n")
f.write("line number is 5\n")
f.write("line number is 6\n")
f.write("line number is 7\n")
f.close()
a_file=open("filename1.txt")
number_of_lines=3
for i in range(number_of_lines):
    line=a_file.readline()
    print(line)
