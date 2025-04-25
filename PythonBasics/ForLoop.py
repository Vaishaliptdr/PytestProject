#For loop used when number of iterations are fixed

obj=[2,3,4,5,6]
for i in obj:
    print(i)
    #print(i*2)
print("****************************************")
#printing sum of first 5 natural numbers (1+2+3+4+5=15)
# if range(i,j)--> i to j-1

summation=0
for i in range(1,6):   #increasing i by 1 after every iteration default case
    print(i)
    summation+=i
print(f"Sum of first five natural numbers is: {summation}")

print("****************************************")

#increasing i by 2 after every iteration
for i in range(1,10,2):    #here 2 is skipping index
    print(i)

print("****************************************")
#Skipping initial index by default it will consider it as 0
for i in range(10):
    print(i)