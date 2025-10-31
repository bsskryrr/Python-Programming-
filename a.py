a = float(input(""))
b = float(input(""))
c= float(input(""))
d = float(input(""))
e = float(input(""))
marks = a+b+c+d+e
print("total marks is", marks)
p = (marks / 500)* 100
print(" percentage is", p)
if p>= 90 :
    print(" grade A")
elif p >= 80 and p< 90 :
    print("grade B")
elif p>= 70 and p< 80 :
    print("grade C")
elif p>= 60 and p<70 :
    print(" grade D")
elif p>= 50 and p< 60:
    print("grade E")
else :
    print("FAIL")