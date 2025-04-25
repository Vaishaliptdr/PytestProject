#Reading file line by line using readlines() method
#readlines() method will copy all content in to list

file=open("test.txt")

listofText=file.readlines()
print(listofText)

for line in listofText:
    print(line)

print(listofText[2])

file.close()
