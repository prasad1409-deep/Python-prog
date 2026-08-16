age = 15
if age <=18:
   print("child")
else:
    print("adult")
print("-----------------------------------------")
#--------------------------------------

marks =83
if marks <=35:
    print("fail")
elif marks >=35:
     print("pass")
elif marks <=85:
     print("first class pass")
     print("---------------------------------------------------")
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
     print("-----------------------------------------------------")

#-------------------------------------
i = 10

if i > 15:
    print("10 is less than 15")
    
print("I am Not in if")
print("-------------------------------------------------")
#-------------------------------------
a=-2
res="positive"if a>0 else "negitive"
print(res)
print("--------------------------------------------------")

#-------------------------------------
#nested if - else
i=10
if i==10:
 if 10<15:
    print("i is smaller than 15")
 if 10<12:
    print("i is smaller than 12")
 else :
    print("i is gratter ")

else :
   print("i is equal to 10")
   print("--------------------------------------------------")

#-------------------------------------------------------
fruits=["apple","banana","mango"]
if "banana" in fruits:
     print("banana is present!")
else :
    print("banana is not present!")
#-----------------------------------------------
"""
username=input("enter the username:").lower()
if username=="admin":
   print("acces granted")
else :
     print("acces denid")
print("--------------------------------------------------")"""
#--------------------------------------------------------------
"""blocklist=["evilbot","troll","spamer"]
username=input("enter the block name:")
if username not in blocklist:
   print(f"welcome,{username}!")
else:
   print("you are in blocklist:-")
print("--------------------------------------------------")"""
#-------------------------------------------------------------

'''username=input("enter the singal:-")
if username=="red":
      print("stop")
if username=="green":
         print("Go")
if username=="yellow":
     print("Get ready")
else:
    print("invaild signal !!!")'''
#----------------------------------------------------------
divce="mackbook"
if divce == "iphone " or divce == "android":
   print("it's is a phone")
elif divce == "mackbook" or divce == "windows":
   print("it's is a lapatop")
else :
   print("unknown divce")
    
























   
