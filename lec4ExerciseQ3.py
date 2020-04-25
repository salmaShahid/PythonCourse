listA = [8,9,10]
listA.remove(8)
listA.insert(0,17) #insert 17 at zero index
# Add 4, 5, and 6 to the end of the list
listB = listA
listB.append(4)
listB.append(5)
listB.append(6)
#Remove the first entry from the list
listC = listB
listC.remove(17)
# Sort the list
listD = listC
listD.sort()
# Double the list
listE = listD*2
#Insert 25 at index 3
listF = listE
listF.insert(3,25)
#manipulate list according to final string
listF.remove(9)
listF.remove(9)
listF.insert(5,17)
listF.append(17)
print("Final List: ",listF) #[4,5,6,25,10,17,4,5,6,10,17]