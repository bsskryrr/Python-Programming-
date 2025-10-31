num = (input(" ")) 
tem= num
sum= 0
n = len(num)
while tem > 0:
    digit = tem %10
    sum += digit**n
    tem //= 10

if sum =num:
       print("armstrong")
else:
    print("not armstrong")
   