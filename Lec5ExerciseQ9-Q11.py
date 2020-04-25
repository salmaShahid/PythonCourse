#Q9- Write a function called matches that takes two strings as arguments and returns how many
# matches there are between the strings. A match is where the two strings have the same character
# at the same index. For instance, 'python' and 'path' match in the first, third, and fourth characters,
# so the function should return 3.
def match(sr1, sr2): #func match have 2 string argumnet
    s1 = set(sr1) #convert in set
    s2 = set(sr2)
    mcs = s1 & s2
    print("No. of matching characters are : " + str(len(mcs))) #return match string


str1 = input("ENter string 1: ") # first string
str2 = input("Enter string 2: ")  # second string

# call count function
print(match(str1,str2))
print("string1: {}, string2: {} ".format(str1,str2))


# Q10- Write a function called change_case that given a string, returns a string with each upper case
# letter replaced by a lower-case letter and vice-versa.

def change_case(): #func which swap change case of string

    lstring = input("Enter lower case string for getting upper case: ")
    print(lstring.swapcase())

    Ustring = input("Enter upper case string for getting lower case: ")
    print(Ustring.swapcase())

# s = input("Enter a string")
# for i in range(len(s)):
#     if s[i].lower():
#         print(s[i].upper())
#     if s[i].upper():
#         print(s[i].lower())

print(change_case())

# Q11- Write a function called is_sorted that is given a list and returns True if the list is sorted and
# False otherwise.
def is_sorted(lt): #take parameter list
    return lt == sorted(lt) #return true or false according to condition

#take list elements  from user
ls=[]
num = int(input("Enter range of list: "))
for _ in range(num):
    pl = input("Enter numbers: ")
    ls.append(pl)

print(ls) #print list
# list= [23,31,55,4,7,8]
print(is_sorted(ls))




#




