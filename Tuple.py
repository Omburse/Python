# Tuple in Python
x = ("Om","Purva","Nikita","Sweety")
y = list(x)
y[1] = "Pungi"
x = tuple(y)
print(x)


#Tuple Method in Python
#Tuple.Count method
tup = (1,2,3,4,5,6,7,8,9,1,2,3,2,2,2,1,1,7,88,8,8,8,)
print("The element are present in a tuple is a count are : ",tup.count(2))

#Tuple Index Method
tup1 = (1,2,3,4,5,6,7,8,9,1,2,3,2,2,2,1,1,7,88,8,8,8,)
print(tup1.index(3))

# Q.1 Write a program to ask the user to enter names of their 3 favorite movies and Store them in a list
#om = input("Enter the first No Movie Name : ")
#om1 = input("Enter the Second No Movies Name :  ")
#om2 = input("Enter the third No Movie Name : ")

#burse = [om,om1,om2]
#print(burse)

#Q.2 Write a program to check if a list is palindrome of element . Using Copy() method
a = [1,2,3,2,1]
print(a.copy())

#Q.3 Write a program to count the no of student with "A" grade in the following tuple ("C","D","A","A","B","B","A")
tup2 = ("C","D","A","A","B","B","A")
print("This element are count No is : ",tup2.count("A"))

#Q.4 Store the above values in a list and sort them from "A" and "D"
list5 = ["A","C","D","B"]
print(list5.sort())
print("The list are ascending order are :",list5)
