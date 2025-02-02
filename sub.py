a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
def add_and_subtract(a, b):
    addition = a + b
    if a > b:
        subtraction = a - b
    else:
        subtraction = b - a
    
sum_result, sub_result = add_and_subtract(a,b)

print("Addition result:", sum_result)
print("Subtraction result:", sub_result)