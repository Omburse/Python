#Next line print to use \n
a = "Om\nUlhas\nBurse"
print(a)

#String length() function
om = "Om"
print(len(om))

#Concatenation in String
p = "Om"
u = "Burse"
print(p+u)

#indexing in string
om4 = "Apna_college"
print(om4[-6])

#Slicing string
str="ApnaCollege"
print(str[:5])

#Negative String
str1 = "Omulhasburse"
print(str1[-10:-5])

#Upper case string
om2 = "burseomulhas"
print("The Upper case method :",om2.upper())

#lower case String
om3 = "OMULHASBURSE"
print("The Lower case method :",om3.lower())
#Strip remove a whitespace
om4 = "   Om    Ulhas     Burse  "
print("The Split method for it Remove a whitespace : ",om4.strip())

#Replace String
om5 = "Hello Om , i love you"
print(om5.replace("Om", "Nikita"))

#write a program to input user first name and print its length

om10 = input("Enter Your Name : ")
print("The length of your name is : ",len(om10))
