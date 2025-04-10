# If-elif-else ladder
a=int(input("enter the age :"))
if(a>=18):
    print("you are above the age of consent")
    print("good for you")

elif(a<0):
    print("you are entering the invalid age")
elif(a==0):
    print("you are entering a invalid age")
else:
    print("you are below the age of consent")
print("end of the program")