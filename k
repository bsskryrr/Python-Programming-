# take integer n if n is odd print Not Weird, if n is and in inclusive rage (2,6)print Weird if n is even and in inclusive range (7, 20) print(Not Weird) if n is even and greater then 20 print(Weird)
n= int(input())
if n%2==0:
   if n is in range(2,6):
      print("Weird)
   if n in range(7,20):
    print("Not Weird")
   if n > 20:
     print("Weird")
else:
  print("Not Weird")
