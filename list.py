friends=["Apple","orange",5,345.6,False,"vibhav","Mike"]

print(friends[4])
friends[0]="graphes"  #replace the item in the list

print(friends)
print(friends[1:4])
friends.append("harry")
print(friends)   #addes the item into list

l1=[1,34,64,78,22,]
l1.sort()
print(l1)       #  sorts the given list 

l1=[1,34,64,78,22,]
l1.reverse()
l1.append("harry")
print(l1)    # reverses the given list

l1=[1,34,64,78,22,]
l1.sort()
l1.insert(1,2244)
print(l1)   # inserts the new item into the list for the given index or position

l1=[1,34,64,78,22,]
# l1.sort()  
#  l1.append("harry")
l1.pop(3)
print(l1)   # pops the given index from the list

l1.remove(1)
print(l1)   #  removes or deletes the item in the list