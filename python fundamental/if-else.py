age = 15
if age <=18:
   print("child")
else:
    print("adult")

#--------------------------------------

marks =83
if marks <=35:
    print("fail")
elif marks >=35:
     print("pass")
elif marks <=85:
     print("first class pass")
     
#--------------------------------------
a = 5
b = 10
c = 7
if a > b and a > c:
   print( a ," a is grater")
elif b > c and b > a:
   print(b, " b is grater")
elif c > a and c > b:
   print( c, "c is grater")
else:
     print(" all no are same")
     
#--------------------------------------
a=int(input("Enter the number a:-"))
b=int(input("Enter the number b:-"))
c=int(input("Enter the number c:-"))

if a > b and a > c:
   print( a ," a is grater")
elif b > c and b > a:
   print(b, " b is grater")
elif c > a and c > b:
   print( c, "c is grater")
else:
     print(" all no are same")

#-------------------------------------
i = 10

if i > 15:
    print("10 is less than 15")
    
print("I am Not in if")
#-------------------------------------
a=-2
res="positive"if a>0 else "negitive"
print(res)
