# program to copy the contents of a file to another file
with open("xyz.txt") as f:
    with open("a1.txt", "w") as f1:
        for line in f:
            f1.write(line)