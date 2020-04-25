#Q13- keys are month names and whose values are the number of days in the corresponding months.
#make dictionary
from functools import reduce

dictionary = {'january' : 31, 'feburary' : 29, 'march' : 31, 'april' : 30, 'may' : 31, 'june' : 30, 'july' : 31, 'august' : 31, 'september' : 30, 'october' : 31, 'november' : 30, 'december' : 31 }

# Ask the user to enter a month name and use the dictionary to tell them how many days
# are in the month.

m=input("Please enter a month name: ")
m=m.lower()
if m in dictionary:
 print('\nThe month ',m,' has ',dictionary[m],'days\n')
else:
 print("the month doesnt exist")

#Print out all of the keys in alphabetical order.
a = sorted(dictionary) #function use to sort all dict items
print("Alphabetical order:  \n")
for s in a:
    print(s)

# Print out all of the months with 31 days
print("\n month have 31 daays: \n")
for m in dictionary:
    if dictionary[m] == 31:
        print(m)

#Print out the (key-value) pairs sorted by the number of days in each month
sv = sorted(dictionary.items(), key=lambda x: x[1]) #pass a lambda function as key function that will return the values of dic in sorted way)
print("\n Print out the (key-value) pairs sorted by the number of days in each month: \n")
for j in range(len(sv)):
    print(sv[j])
# spell the first three letters of
# the month name correctly
m=input("Please enter a month name: ").lower()
newdic = {'jan': 'january','feb': 'feburary', 'mar': 'march', 'apr': 'april', 'may':'may','jun' : 'june', 'jul': 'july','aug': 'august', 'sep': 'september','oct': 'october', 'nov': 'november','dec': 'december'}
import datetime
print(datetime.datetime.strptime(m,'%b').strftime('%B'))


#Q14-Write a program that uses a dictionary that contains ten user names and passwords. The
# program should ask the user to enter their username and password. If the username is not
# in the dictionary, the program should indicate that the person is not a valid user of the
# system. If the username is in the dictionary, but the user does not enter the right password,
# the program should say that the password is invalid. If the password is correct, then the
# program should tell the user that they are now logged in to the system.


U = {'salma': '123',
    'sana' : '456',
    'asad': '564',
    'alia': '234',
    'zunaira': '134',
    'abdullah': '678',
     'razi': '765',
     'mishaal': '987',
     'shahid': '786',
     'samad':'812'}


storU = U

username_password = storU
print("Python !\n")
name = str(input("Please enter your preferred username.\n"))
passcode = str(input("Thank you, now enter a password as well.\n"))
username_password[name] = passcode
print(username_password)

login_username = str(input("Please enter your username.\n"))
login_password = str(input("Please enter your password.\n"))

if username_password.get(login_username) == login_password:
    # Correct username and password match
    print("welcome")
else:
    # Incorrect username/password match
    print("wrong")


#Q15- Repeatedly ask the user to enter a team name and the how many games the team won
# and how many they lost. Store this information in a dictionary where the keys are the team
# names and the values are lists of the form [wins, losses]

n = int(input("Enter number of teams : "))
scores = {} #empty dic
for i in range(n):
    name = input("enter team name : ")
    w = int(input("enter wins : "))
    l = int(input("enter losses : "))
    scores[name] = [w, l]
    print(scores)


# Using the dictionary created above, allow the user to enter a team name and print out the team’s winning percentage.
t = input("enter team name : ")
print("winning percentage of", t, "is", (scores[t][0]/sum(scores[t]))*100)

#Using the dictionary, create a list whose entries are the number of wins of each team.
w_team = [i[0] for i in scores.values()]
print(w_team)

#Using the dictionary, create a list of all those teams that have winning records
w_rec = []
for i in scores:
    if scores[i][0] > 0:
        w_rec.append(i)
    print(w_rec)

#
# # Q16- Repeatedly ask the user to enter game scores in a format like team1 score1 - team2 score2.
# # Store this information in a dictionary where the keys are the team names and the values are
# # lists of the form [wins, losses]
#
n = int(input("Enter number of teams : "))
scores = {} #empty dic

for i in range(n):
    name = input("enter team name : ")
    w = int(input("enter wins : "))
    l = int(input("enter losses : "))
    scores[name] = [w, l]
    print(scores)


#Q17-  Dictionaries provide a convenient way to store structured data. Here is an example
# dictionary:
d=[{'name':'Todd', 'phone':'555-1414', 'email':'todd@mail.net'},
{'name':'Helga', 'phone':'555-1618', 'email':'helga@mail.net'},
{'name':'Princess', 'phone':'555-3141', 'email':''},
{'name':'LJ', 'phone':'555-2718', 'email':'lj@mail.net'}]

# All the users whose phone number ends in an 8
for i in range(0,4):
    p = d[i]
    g = p.get('phone')
    if g[-1] == '8':
        print("Phone number : {} and the name of user: {} ".format(g, p.get('name')))


# All the users that don’t have an email address listed
for i in range(0,4):
    p = d[i]
    g = p.get('email')
    if g == '':
        print("the name of user {} has empty mail ".format(p.get('name')))
