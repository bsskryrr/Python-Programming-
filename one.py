a = float(input (""))
b = float(input(""))
ch = float(input(" enter choice"))
if ch == 1 :
    c= a+b
    print("addition is ", c)
elif ch == 2 :
    c= a- b
    print("subtraction ", c)
elif ch == 3 :
    c = a* b
    print("multipliction is ", c)
elif ch ==  4 :
    c = a/b
    print (" division is ", c)
else :
     print(" wrong choice ")