
str="Vaishalipotdar@gmail.com"
str1="VaishaliPotdar"
str3="Vaishali"
str4=" Great "

print(len(str))             #printing length of the string
print(str[1])               #printing char at index 1
print(str[0:9])             #printing substring from index 0 to 9
print(str1+str4)            #conctenating 2 strings
print(str3 in str)          #checking weather str3 present in str

var=str.split(".")          #spilinting string at mentioned char and store at var
print(var)
print(var[0])               #printing substring at index 0
print(var[1])               #printing substring at index 0

print(str4.strip())         #removing blank spaces from start and last of string
print(str4.lstrip())        #removing blank spaces from left of string
print(str4.rsplit())        #removing blank spaces from right of string

#It returns a string with the first letter capitalized, that is, in upper case, and the
# other characters of that string are converted to lower case letters
str5="keshav"
print(str5.capitalize())     #making first letter capital case
print(str.count("a",0))         #counting char a staring from 0th index
print(str.replace("potdar","dusane"))    #replacing string with mentioned string
print(str.upper())              #converting string to upper case
print(str.lower())              #converting string to lower case

