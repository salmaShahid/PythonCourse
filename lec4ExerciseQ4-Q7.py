#Q4-Ask the user to enter a list containing numbers between 1 and 12. Then replace all of the
# entries in the list that are greater than 10 with 10.
lis = []
for i in range(0,12):
    z = int(input("enter num "))
    lis.append(z)
#list comprehension method
p = 10
if p >10:
    pass
else:
    w = [10 if x>10 else x for x in lis]
    print("Final list: ",w)

#Q5-Ask the user to enter a list of strings. Create a new list that consists of those strings with
#their first characters removed.
#
list = []
userN = input("enter your name: ")
userC = input("enter your class: ")
userU = input("enter your University name: ")

list.append(userN)
list.append(userC)
list.append(userU)
print("First list: ",list)
list2 =[]
for i in list:
    s = i[1:]
    list2.append(s)
print("Second List: ",list2)

#Q6- a program that takes any two lists L and M of the same size and adds their elements
#together to form a new list N whose elements are sums of the corresponding elements in L
# and M. For instance, if L = [3,1,4] and M = [1,5,9], then N should equal [4,6,13].

L = []
user1 = int(input("enter num1: "))
user2 = int(input("enter num2: "))
user3 = int(input("enter num3: "))

L.append(user1)
L.append(user2)
L.append(user3)
print("First list: ",str(L))

M = []
user1 = int(input("enter num1: "))
user2 = int(input("enter num2: "))
user3 = int(input("enter num3: "))

M.append(user1)
M.append(user2)
M.append(user3)
print("Second list: ",str(M))

N = []
for j in range(3):
    N.append(L[j] + M[j])
print("\nThe total Sum of Two Lists =  ", N)


#Q7- . When playing games where you have to roll two dice, it is nice to know the odds of each
# roll. For instance, the odds of rolling a 12 are about 3%, and the odds of rolling a 7 are about
# 17%. You can compute these mathematically, but if you don’t know the math, you can write
# a program to do it. To do this, your program should simulate rolling two dice about 10,000
# times and compute and print out the percentage of rolls that come out to be 2, 3, 4, . . , 12.

import random
count = [0, 0, 0, 0, 0, 0] #make siple zero list for  count purpose
for i in range(10000): #roll dice 10000 time
    count[random.randint(0, 5)] += 1 #it will generate random num and place it in count list
for i in range(6):#get first 6 values result
    print("Value %d happened %d times" % (i + 1, count[i])) #print those values