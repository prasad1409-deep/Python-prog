marks=int(input("Enter your marks:-
                "))
if marks>=90:
    print(marks,"grade A")
elif marks>=80 and marks<=89:
    print(marks,"grade B")
elif marks>=70 and marks<=79:
    print(marks,"grade C")
elif marks>=60 and marks<=69:
    print(marks,"grade D")
elif marks<=60:
    print(marks,"fail!!")
