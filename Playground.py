#Lambda/Anon Functions:

x = lambda y:y+2 #this first y is the bound variable and the second is the body
#to use: 
print(x(10)) # will give 12

# or you can do it with more arguments:
z = lambda a,c:a*c
print(z(20,40))