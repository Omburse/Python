marks = [6.69 , 7.5 , 8.69 , 7.8]
print(type(marks))
print(marks)

stu = ["Om",22,"Pune"]
stu[0] = "Purva"
print(stu)
print("The Student name is : ",stu[0])
print("The Student age is : ",stu[1])
print("The Student address is : ",stu[2])

#List Methods


list1 = [1,4,5,6,2,3]

#append means add element at the end index

list1.append(10)
print("The list append method is : ",list1)

#reverse means list descending order

list1.sort(reverse=True)
print("The reverse Method is : ",list1)

#Sort means list ascending order

print(list1.sort())
print(list1)

#Reverse a list to use .reverse() method

list1.reverse()
print("The reverse a list is : ",list1)

#To add a Index wise element

list1.insert(2,75)
print("The index 2 add a element 75 : ",list1)

