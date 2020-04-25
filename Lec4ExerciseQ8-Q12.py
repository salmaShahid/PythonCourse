#Q8- Write a program that asks the user to enter some text and then counts how many articles
# are in the text. Articles are the words 'a', 'an', and 'the'.

tk = input("enter string :" )
t = tk.count('the')
a = tk.count('a')
n = tk.count('an')
print("number of *the* is: {} , number of *a* is: {}, number of *an* is: {}".format(t,a,n))

# Q9- (a) Write a program that asks the user to enter a sentence and then randomly rearranges
# the words of the sentence. Don’t worry about getting punctuation or capitalization correct.

from random import shuffle
u = input("Enter a sentence")
split = u.split()  # Split the string into a list of words
shuffle(split)  # This shuffles the list in-place.
j = ' '.join(split) #the list back into a string
print("Suffle Strings:  ",j)

# #(b) Do the above problem, but now make sure that the sentence starts with a capital, that the
# # original first word is not capitalized if it comes in the middle of the sentence, and that the
# # period is in the right place
#
sentences = u.split(". ")
sentences2 = [sentence[0].capitalize() + sentence[1:] for sentence in sentences]
string2 = '. '.join(sentences2)

print ("Final Sentence with capiatalize: ",string2)


# Q10-Write a censoring program. Allow the user to enter some text and your program should
# print out the text with all the curse words starred out. The number of stars should match the
# length of the curse word. For the purposes of this program, just use the “curse” words darn,
# dang, freaking, heck, and shoot.

extract = input("Enter text:  ") #Oh shoot, I thought I had the dang problem figured out. Darn it. Oh well, it was a heck of a freaking try.
censored_sent = "shoot"
s =  extract.replace(censored_sent, "*" * len(censored_sent))
# sent = "Go feed all the ducks in the lake"
censored_sent1 = "dang"
w = s.replace(censored_sent, "*" * len(censored_sent1))
censored_sent2 = "freaking"
x = w.replace(censored_sent1, "*" * len(censored_sent2))
censored_sent3 = "Darn"
y = x.replace(censored_sent2, "*" * len(censored_sent3))
censored_sent4 = "heck"
f = y.replace(censored_sent3, "*" * len(censored_sent4))
print("final: ",f)

#Q11-Write a program that repeatedly asks the user to enter product names and prices. Store
# all of these in a dictionary whose keys are the product names and whose values are the prices.
# When the user is done entering products and prices, allow them to repeatedly enter a product
# name and print the corresponding price or a message if the product is not in the dictionary

def getPro():
    name = input("enter Product name")
    price = input("enter product price")
    dicts= {
        'name':name,
        'price' : price,
    }
    return dicts

std = []
while True:
    print("1 : add product and prices")
    print("2 : display all product")
    print("3 : search product")
    print("4: Enter dollar Amount and print all product whose price<that amount")
    print("5 : end")

    choice = int(input("enter what operation you choose"))
    if choice == 1:
        my_Pro = getPro()
        std.append(my_Pro)
    elif choice == 2:
        print(std)
    elif choice == 3:
        s = input("enter key  you want to search from dictionary ")
        for i in std: #list with loop if multi entries
            if i['name'] == s:
                print(i['name'])
                break
            else:
                print("Invalid Product")
    # Q12- Using the dictionary created in the previous problem, allow the user to enter a dollar
    # amount and print out all the products whose price is less than that amount.
    elif choice == 4:
        d = int(input("Enter Dollar$ price: "))
        for j in std:
            if j['price'] < str(d):
                print(j['name'])
                break
            else:
                print("Sorry")
    elif choice == 5:
        break

