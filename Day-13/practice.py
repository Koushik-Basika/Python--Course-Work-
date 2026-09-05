'''
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
else:
    print("Negative")


num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


num = int(input("Enter a number: "))
if num % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 5")   


num = int(input("Enter a number: "))
if num % 3 == 0 and num % 7 == 0:
    print("Divisible by both 3 and 7")
else:
    print("Not divisible by both 3 and 7")


a= int(input("Enter year: "))
if (a % 400 == 0) or (a % 4 == 0 and a % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")


marks = int(input("Enter marks: "))
if marks >= 35:
    print("Pass")
else:
    print("Fail")


a= int(input("Enter a number: "))
if 100 <= abs(a) <= 999:
    print("3-digit number")
else:
    print("Not a 3-digit number")


ch = input("Enter a character: ")
if ch in "aeiouAEIOU":
    print("Vowel")
else:
    print("Consonant")


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print(a, "is greater")
else:
    print(b, "is greater")


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a < b:
    print(a, "is smaller")
else:
    print(b, "is smaller")
    

a = int(input("Enter a number: "))
if a == 0:
    print("Number is Zero")
else:
    print("Number is Not Zero")


a = int(input("Enter a number: "))
if a % 10 == 0:
    print("Multiple of 10")
else:
    print("Not a Multiple of 10")


a = int(input("Enter age: "))
if a >= 18:
    print("Eligible to Vote")
else:
    print("Not Eligible to Vote")


a= int(input("Enter a number: "))
if 10 <= a <= 50:
    print("Number is in the range")
else:
    print("Number is not in the range")


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a == b * b:
    print(a, "is the square of", b)
elif b == a * a:
    print(b, "is the square of", a)
else:
    print("Neither number is the square of the other")


str1 = input()
str2 = input()
if str1 == str2:
    print("Strings are Equal")
else:
    print("Strings are Not Equal")


num = int(input("Enter a number: "))
if num > 1:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print("Prime Number")
    else:
        print("Not a Prime Number")
else:
    print("Not a Prime Number")


a = int(input("Enter a number: "))
if a > 0 and a % 2 == 0:
    print("Positive and Even")
else:
    print("Condition Not Satisfied")


ch = input("Enter a character: ")
if 'A' <= ch <= 'Z':
    print("Uppercase Letter")
elif 'a' <= ch <= 'z':
    print("Lowercase Letter")
else:
    print("Not an Alphabet")


temp = int(input("Enter temperature: "))
if temp > 30:
    print("It's Hot")
else:
    print("It's Not Hot")


a = int(input("Enter a number: "))
if 1000 <= abs(a) <= 9999 and a % 2 == 0:
    print("4-digit Even Number")
else:
    print("Not a 4-digit Even Number")


ch = input("Enter a character: ")
if ch.isalpha():
    if ch not in "aeiouAEIOU":
        print("Consonant")
    else:
        print("Vowel")


a = int(input("Enter a number: "))
if a % 2 == 0 and a % 3 == 0:
    print("Divisible by both 2 and 3")
else:
    print("Not divisible by both 2 and 3")


a = int(input("Enter a number: "))
if a % 2 == 0 and a % 3 != 0:
    print("Divisible by 2 only")
else:
    print("Condition Not Satisfied")


a = int(input("Enter a number: "))
if a < 0 and a % 2 != 0:
    print("Negative and Odd")
else:
    print("Condition Not Satisfied")


a = input("Enter a string: ")
if a[0] in "aeiouAEIOU":
    print("Starts with a Vowel")
else:
    print("Does Not Start with a Vowel")


a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))
if a + b > c and a + c > b and b + c > a:
    print("Valid Triangle")
else:
    print("Invalid Triangle")


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a >= b and a >= c:
    print(a, "is the Greatest")
elif b >= a and b >= c:
    print(b, "is the Greatest")
else:
    print(c, "is the Greatest")


a = int(input("Enter year: "))
if a % 100 == 0 and a % 400 == 0:
    print("Century Leap Year")
else:
    print("Not a Century Leap Year")


a = input("Enter a character: ")
if a.isdigit():
    print("Digit")
else:
    print("Not a Digit")


a = int(input("Enter a number: "))
original = a
reverse = 0
while a > 0:
    digit = a % 10
    reverse = reverse * 10 + digit
    a = a // 10
if original == reverse:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")


str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
if len(str1) > len(str2):
    print("First string is longer")
elif len(str1) < len(str2):
    print("Second string is longer")
else:
    print("Both strings have equal length")


a = int(input("Enter a number: "))
if 50 <= a <= 100 and a % 5 == 0:
    print("Number is in range and divisible by 5")
else:
    print("Condition Not Satisfied")


a = input("Enter password: ")
if len(a) >= 8:
    print("Strong Password")
else:
    print("Weak Password")


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
total = a + b
if total % 2 == 0:
    print("Sum is Even")
else:
    print("Sum is Odd")


a = input("Enter a character: ")
if not a.isalnum():
    print("Special Character")
else:
    print("Not a Special Character")


a = int(input("Enter temperature: "))
if a < 15:
    print("Cold")
elif a <= 30:
    print("Moderate")
else:
    print("Hot")


a = int(input("Enter a number: "))
if a < 10 or a > 50:
    print("Outside the Range")
else:
    print("Inside the Range")


a = int(input("Enter a number: "))
root = int(a ** 0.5)
if root * root == a:
    print("Perfect Square")
else:
    print("Not a Perfect Square")


a = int(input("Enter first person's age: "))
b = int(input("Enter second person's age: "))
if a > b:
    print("First person is older")
elif b > a:
    print("Second person is older")
else:
    print("Both are of the same age")


a= int(input("Enter an angle: "))
if a < 90:
    print("Acute Angle")
elif a == 90:
    print("Right Angle")
elif a < 180:
    print("Obtuse Angle")
else:
    print("Invalid Angle")
'''