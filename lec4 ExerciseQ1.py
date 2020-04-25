# # program that asks the user to enter a list of integer
print("????????????????? Question1 ////////////////\n")
lis = []
n = int(input("Enter number of elements you want to save in list : "))
for id in range(n):
    num = int(input("enter numbers: "))
    lis.append(num)

# Print the total number of items in the list.
print("list: ",lis)

# Print the last item in the list
print("Last digit of List: ",lis[-1])

#Print the list in reverse order.
print("using slicing reverse List: ",lis[::-1]) #start:end:step


print("using for loop with built in reversed function")
for item in reversed(lis):
    print(item)

#Print Yes if the list contains a 5 and No otherwise
print("search 5 yes else no: \n")
if 5 in lis:
    print("\tyes 5 appear ")
else:
    print("\tno 5 not appear")

#Print the number of fives in the list.
c = lis.count(5)
print("Number of 5 in list: ",c)

# Print how many integers in the list are less than 5
k = 5
count = 0
for i in lis:
    if i < k:
        count = count + 1
print("The numbers less than 5 : " + str(count))

# Remove the first and last items from the list, sort the remaining items, and print the result using pop(0) to perform removal
lis.pop(0)
lis.pop(-1)
print("sorted list by removing first or last element: ",sorted(lis))
