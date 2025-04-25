#While loop used when number of iterations are not fixed

a=4

while a>1:
    print(a)
    a=a-1

print("****************************************")

a=5

while a>1:
    if a!=3:
        print(a)
    a=a-1

print("****************************************")

# break statement abruptly stops the execution of program
a=5

while a>1:
    if a==3:
        break
    print(a)
    a=a-1

print("****************************************")
# Continue statement will skip current iteration and execute next iteration

a=10
while a>1:
    if a==9:
        a = a - 1
        continue  #Skip this step from while loop
    if a==3:
        break   #breaks entire while loop
    print(a)
    a=a-1