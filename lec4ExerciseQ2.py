# program that generates a list of 20 random numbers between 1 and 100. Print the list.
import random #lib random
a=[] #create empty list
n=20 #no of element by user as 20
for j in range(n):
    a.append(random.randint(1,100))
print('Randomised list is: ',a) #a part
lst = a
average = sum(lst)/len(lst)

# Printing average of the list
print("Average of the list =", round(average, 2)) #b part

#Print the largest and smallest values in the list
print("Maximum element in the list is :", max(a), "\nMinimum element in the list is :", min(a)) #c part

#Print the second largest and second smallest entries in the list
l = len(a)
# mlist = list(set(a))
print("Second Largest element is:", a[-2])
print("Second Smallest element is:", a[1])

#Print how many even numbers are in the list
e, o = 0,0
for num in a:
    if num % 2 == 0:
        e += 1
    else:
        o += 1
print("Even numbers in the list: ", e)
print("Odd numbers in the list: ", o)

