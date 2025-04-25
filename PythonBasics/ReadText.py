#Reading from text file

file=open("test.txt")
print(file.read())    #reading entire content of file

print(file.read(5))    #reading first 5 characters from file  #Hello


#readline and read function should not be used together
#if want to run any function, comment another one

print(file.readline())  #reading first line
print(file.readline())  ##reading second line

file.close()