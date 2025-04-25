#read the file and store data in list
#now reverse the list and write it to file

#we can open file as "file=open("test.txt")" but here we need to close it also
#but if we open file as "with open("test,txt") as file:" it will close automatically
# after completing execution

with open("test.txt","r") as reader:
    content=reader.readlines()
    reverseContent=reversed(content)
    print(reverseContent)

    with open("test.txt", "w") as writer:
        for line in reverseContent:
            print(writer.write(line))


