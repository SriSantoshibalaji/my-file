input_number = 28
sum = 0
for i in range(1,input_number):
   if (input_number % i == 0):
      sum = sum + i
if (sum==input_number):
   print("perfect number")
else:
   print("not perfect number")
