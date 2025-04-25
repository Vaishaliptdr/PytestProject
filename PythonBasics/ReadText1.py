#Reading file line by line using readline() method

file=open("test.txt")

line=file.readline()

while line !="":
    print(line)
    line=file.readline()

file.close()
