year=int(input("enter a number:"))
if year % 4==0:
   if year % 100!=0 or year%400==0:
      print("leap year")
else:
   print("not leap year")