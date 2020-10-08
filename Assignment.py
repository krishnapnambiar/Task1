#task 1 -python program to find the largest number in a list
list1 = [1,5,50,400,99,68]
print ("largest number in a list is : ", max(list1))

#task2  -python program to find the second largest number in a list
list1 = [1,5,50,400,99,68]
list1.sort()
print ("second largest number in the list is : ", list1[-2])

#task3 - python program to merge two lists and sort it
list1 = [15, 25, 96, 69, 11] 
list2 = [36, 432, 74, 48, 10] 
print ("The original list 1 is : ",list1) 
print ("The original list 2 is : ",list2) 
list3 = sorted(list1 + list2) 
print ("The combined sorted list is : ",list3) 

#task4 - python program to swap the first and last value of a list
list = [10,2,3,4]
temp = list [0]
list[0]= list[3]
list[3]= temp
print (list)
