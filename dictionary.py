d={}  #empty dictionary

#   dictionary 

marks = {
    "harry":100,
    "shubham":90,
    "rohan":23
}
print(marks,type(marks)) 

print(marks["shubham"])

# dictionary methods 
marks = {
    "harry":100,
    "shubham":90,
    "rohan":23,
    0:"harry"
}
print(marks.items()) 
print(marks.keys())
print(marks.values())
marks.update({"harry":99,"rehuka":47})
print(marks.get("rohan"))
print(marks)

# difference
print(marks["shubham"])  #prints None
print(marks.get("rohan"))   #returns error