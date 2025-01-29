num=int(input("enter a number:"))
if num==1:
   print("nither prime nor composite")
else:
   print("not prime")
if num>1:
   for n in range(2,num):
      if num%n==0:
         print("not prime")
else:
   print ("prime")