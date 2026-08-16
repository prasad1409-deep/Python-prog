unit=int(input("unit consumed:-"))
if unit<=100 :
    rate=5
 
elif unit>100 and unit<=300:
    rate=7
 
elif unit>=300:
    rate=10
    
bill=unit*rate
print(bill)
age =int(input("senior citizen check:-"))

if age>=60:
    discount=bill*0.2
    print("discount value=",discount)
else:
    discount=0
    print("discoubt value=",discount)
final_bill = bill - discount
print("final_bill= bill - discount")
print(final_bill)
