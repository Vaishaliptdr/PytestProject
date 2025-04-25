# List is data type having multiple values with different datatypes
# List is mutable: we can update after defining the list

values=[1,2,"Arnav",4,5]

#Printing values of list
print(values)            # 1,2,Arnav,4,5
print(values[0])         #1
print(values[2])         #Arnav
# print(values[8])       error list index out of range
print(values[-1])        #5
print(values[-2])        #4
print(values[-3])        #Arnav


#Printing values of list mentioned in range (last range is excluded)
print(values[1:3])       #[2, 'Arnav']
print(values[2:4])       #['Arnav', 4]

#Inserting new values to list at mentioned index
values.insert(3,"Potdar")
print(values)

#Appending values to list at last index
values.append("End")     #[1, 2, 'Arnav', 'Potdar', 4, 5]
print(values)            #[1, 2, 'Arnav', 'Potdar', 4, 5, 'End']

#Updating values from list with mentioned index
values[2]="Aditya"
print(values)            #[1, 2, 'Aditya', 'Potdar', 4, 5, 'End']

#Deleting values from list
del values[1]
print(values)            #[1, 'Aditya', 'Potdar', 4, 5, 'End']
