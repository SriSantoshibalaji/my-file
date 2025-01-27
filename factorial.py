def fact(n):
   if(n==1):
      return 1
   else:
      return n*fact(n-1)
n=int(input("enter the number to find factorial"))
Fact=fact(n)
print("Factorial value is",Fact)