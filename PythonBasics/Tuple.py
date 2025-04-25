# Tuple is data type having multiple values with different datatypes
# Tuple is immutable: we can not update after defining the Tuple

values=(1,2,"Arnav",4,5)

#Printing values of tuple
print(values)                  #(1, 2, 'Arnav', 4, 5)
print(values[1])               #1
print(values[-1])              #5


#Updating will result in to error as we can not update tuple after creation
#values[2]="Aditya"
print(values)