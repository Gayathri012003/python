#square or cube
ope = input("enter square or cube: ").lower()
while True:  
    if ope == "square":
        n = int(input("enter a number: "))
        print("square of a number:", n**2)
    elif ope == "cube":
        n = int(input("enter a number: "))
        print("cube of a number:", n**3)
    elif ope == "exit":
        break
    else:
        print("invalid input")  
    ope = input("enter square or cube (or 'exit' to quit): ").lower()
#palindrome
num=int(input("enter a number: "))
temp=num
rev=0
while temp>0:
    rem=temp%10
    rev=rev*10+rem
    temp=temp//10
if num==rev:
    print("palindrome")
else:
    print("not palindrome")
#string palindrome
text=input("enter a string:")
b=""
for i in text:
    b=i+b
if text==b:
    print("palindrome")
else:
    print("not palindrome")
#perfect number
n=int(input("enter a number: "))
sum=0
for i in range(1,n):
    if n%i==0:
        sum=sum+i
if n==sum:
    print("perfect number")
else:
    print("not perfect number")
#GCD
a=int(input("enter a number:"))
b=int(input("enter a number:"))
while b:
    temp=a%b
    a=b
    b=temp
gcd=a
print("gcd of a number:",gcd)

# LCM 
x = int(input("Enter the first number:"))
y = int(input("Enter the second number"))
if x > y:
    big = x
else:
    big = y
while True:
    if (big % x == 0) and (big % y == 0):
        LCM = big
        break
    big = big + 1
print("LCM of two numbers is:", LCM)

