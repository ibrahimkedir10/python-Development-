list = ["ib" ,"jim", "bob"]
list2 = [1,1,1,2,3,4,5,6,7,8,9,10]


print(list) # print list
print(list[0]) #print index 0
print(list2[-1]) # print index 1 starting from the back
print(list2[:5]) #print every number before 5
print(list2[5:]) #print every number after 5
print(list2[2:4]) # print using range
list.extend(list2) # add 2 list together 
print(list)
list.append("max")
print(list)
list.insert(1, "boo")
print(list)

## POP (remove last index) [last in list out]
list.pop()
print(list)

list.reverse() #revese list
print(list)

print(list2.count(1)) #count the number of 1's 
