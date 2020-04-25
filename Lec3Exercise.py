#convert decimal to binary
print("???????????????? DECIMAL TO BINARY //////////////////// \n")
# prompt user to enter decimal number
DecimalNumber = int(input("Enter any decimal number: "))
# using bin function convert binary to decimal
print("Equivalent Binary Number: ", bin(DecimalNumber))
#

print("???????????????? ENCRYPT AND DERYPT DATA //////////////////// \n")

#encrypt and Decrypt
# Simple way
#encryption
res = [] #make simple list
sentence = input("Enter any input string for encryption: ")
for letter in sentence: #loop for getting avery charcter ascii code of sentence
    l = ord(letter) - 20 #to encrypt minus 20 from ascii code of every letter
    res.append(l) #append in the end index of list

print("This is encrypted message!")
for numbers in res: #loop to remove list effect from res
    print(numbers, end='')
    print(" ",end='')

"""
the ascii code of h is 104, if we subtract with 20 then it will be 84 
so no one know the actual data.Decryption is the opposite way of encryption. 
"""

#for decryption
end_string = ""
for numbers in res:
    l = int(numbers) #convert in integer
    l = l + 20 #add 20
    l=chr(l) #convert into charcter
    end_string = end_string + l

print("\nThis is decrypted form: {}".format(end_string))


# Fibonacci sequence up to n-th term
# the nth term is the sum of (n-1)th and (n-2)th term
print("???????????????? FIBONACCI SEQUENCE //////////////////// \n")
User = int(input("How many terms? ")) #take input value from user and do type casting
# first two terms are zero and one
n1, n2 = 0, 1
count = 0 #used as counnter of loop
# check if the number of terms is valid
if User <= 0: #it is impossible to get neg value fibonacci according to condition
    #  so first check it whether num is pos,neg
   print("Please enter a positive integer")
elif User == 1: #if it is = 1 then ans is 0 bcz it shows according to  sequence val
   print("Fibonacci sequence upto",User,":")
   print(n1) #0
else: #otherwise
   print("Fibonacci sequence:")
   while count < User: #make loop 0< user value then print 1 and then proceed accorsing to sequential values fibonaci
       print(n1)
       nth = n1 + n2 #nth=0+1 like
       # update values
       n1 = n2 #0=1 like
       n2 = nth #1 = nth value like
       count += 1 #count = count + 1 (for preventing unstopable loop)
