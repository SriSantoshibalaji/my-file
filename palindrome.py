
def ispalindrome(string):
    if string==string[::-1]:
       print("palindrome")
    else:
        print("not palindrome")
string=input("enter a string")
print(ispalindrome(string))