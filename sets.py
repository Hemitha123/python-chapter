# s={1,3,55,765}  
# print(s)

# #  e=set()  # don't use s={} as it will create an empty dictionary

# sets methods 

s={1,3,5,5,765,"harry"}
print(s, type(s))
s.add(635)
s.remove(5)
s.pop()
print(s,type(s))

# set union intersection 

s1={1,45,6,78}
s2={7,8,1,78}
print(s1.union(s2))
print(s1.intersection(s2))

