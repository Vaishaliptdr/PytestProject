# Dictionary s datatype having key value pairs
#If key or value is a string then need to mention in "" or ''

dict ={"a":1, 3:"Arnav","c":"Potdar"}
print(dict["a"])                #1
print(dict[3])                  #Arnav
print(dict["c"])                #Potdar
print(dict)                     #'a': 1, 3: 'Arnav', 'c': 'Potdar'}


#Creating dictionaries at run time and adding data to it

dict={}
dict["FirstName"]="Arnav"
dict["LastName"]="Potdar"
print(dict)                     #{'FirstName': 'Arnav', 'LastName': 'Potdar'}

dict["Age"]=10
print(dict)                     #{'FirstName': 'Arnav', 'LastName': 'Potdar', 'Age': 10}

print(dict["FirstName"])        #Arnav
print("First name:",dict["FirstName"])   #First name: Arnav