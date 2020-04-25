#1 Write a function called rectangle that takes two integers m and n as arguments and prints out an
# m × n box consisting of asterisks. Shown below is the output of rectangle(2,4)
def rec (m,n):
    print('*' * m * m) #****
    print("*" * n)#****
    return m*n
width=int(input('Input the width: ')) #2
height=int(input('Input the height: '))#4

print(rec(width,height))

#Q2- (a) Write a function called add_excitement that takes a list of strings and adds an exclamation
# point (!) to the end of each string in the list. The program should modify the original list and not
# return anything.

sentence_list = ["Four score and seven years ago, our fathers brought forth on",
                 "this continent a new nation, conceived in liberty and dedicated",
                 "to the proposition that all men are created equal.  Now we are",
                 "   engaged in a great        civil war, testing whether that nation, or any",
                 "nation so conceived and so dedicated, can long endure"]
def exclam():
    for i in range(0,4):
        print(sentence_list[i],"!") #in last print ! sign

print(exclam())

#(b) Write the same function except that it should not modify the original list and should instead
# return a new list.

nl= []
def exclam():
    for i in range(0,4):
        print(sentence_list[i],"!")
        nl.append(sentence_list[i])
    return nl
print(exclam())

#Q3-Write a function called sum_digits that is given an integer num and returns the sum of the digits
# of num.

def sd(a,b):
    return a+b

dg1 = int(input("Enter num1: "))
dg2 = int(input("Enter num2: "))
print("Sum of digit is: ",sd(dg1,dg2))

#Q4- The digital root of a number n is obtained as follows: Add up the digits n to get a new number.
# Add up the digits of that to get another new number. Keep doing this until you get a number that
# has only one digit. That number is the digital root.
# For example, if n = 45893, we add up the digits to get 4 + 5 + 8 + 9 + 3 = 29. We then add up the
# digits of 29 to get 2 + 9 = 11. We then add up the digits of 11 to get 1 + 1 = 2. Since 2 has only
# one digit, 2 is our digital root.
# Write a function that returns the digital root of an integer n. [Note: there is a shortcut, where the
# digital root is equal to n mod 9, but do not use that here.]

def digit(n): #fun of digital root find
    if len(n) == 1:
        return n
    else:
        sum = 0
        for i in n:
            sum += int(i)
        num = str(sum)
        return digit(num)

#1234-> 1+2+3+4 = 10, 10-> 1+0=1, 1-> 1
n= input("Enter your number: ")
print(n)
print("The digital root of ", n, " is: ", digit(n))


# Q5- Write a function called first_diff that is given two strings and returns the first location in which
# the strings differ. If the strings are identical, it should return -1.

def first_dff(a,b):
    for c in a:
        ord(c)
    for c in b:
        ord(c)
    if a == b: #if same
        return -1
    else:
        x = [i for i in range(len(a)) if a[i] != b[i]] #length of a must be same as b
        return x

s1 = input("enter string one: ")
s2 = input("enter string two: ")

# print(x)
print(first_dff(s1,s2))


#Q6- Write a function that takes an integer n and returns a random integer with exactly n digits. For
# instance, if n is 3, then 125 and 593 would be valid return values, but 093 would not because that
# is really 93, which is a two-digit number.


# generate random integer values
from random import randint
def random(n):
   st = 10 ** (n-1) #strating
   en= (10**n)-1 #ending
   return randint(st,en)

l = int(input("Enter limit"))
print(random(l))

#Q7- Write a function called number_of_factors that takes an integer and returns how many factors
# the number has.
def factr(x):
   for i in range(1, x + 1): #for loop to iterate from i equal to x.
       if x % i == 0:#If x is perfectly divisible by i, it's a factor of x.
           print(i)

num = int(input("Enter num for finding factor: "))
print("These are the factors of",num)
print(factr(num))


#Q8- Write a function called closest that takes a list of numbers L and a number n and returns the
# largest element in L that is not larger than n. For instance, if L=[1,6,3,9,11] and n=8, then the
# function should return 6, because 6 is the closest thing in L to 8 that is not larger than 8. Don’t
# worry about if all of the things in L are smaller than n

ls = []
def closest():
    n = int(input("Enter num"))
    num = int(input("Enter range of list: "))
    for _ in range(num):
        pl = input("Enter numbers: ")
        ls.append(pl)

    print(ls)
    # ls.append(l)
    # print(ls)
    for i in range(4):
        if int(ls[i]) < n:
            print(ls[i])

        return ls[i]
print(closest())
