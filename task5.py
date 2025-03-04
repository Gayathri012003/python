a=5
if a>0:
    print("a is positive")
print("time complexity-O(1)")
print("space complexity-O(1)")
#else condition
a=5
if a<0:
    print("a is negative")
else:
    print("a is positive")
print("time complexity-O(1)")
print("space complexity-O(1)")
#elif
a=-10
if a==0:
    print("a is zero")
elif a>0:
    print("a is positive")
else:
    print("a is negative")
print("looping statements--------------------")
print("time complexity-O(1)")
print("space complexity-O(1)")
#while loop
a=1
while a<6:
    print(a)
    a=a+1
print("time complexity-O(1)")
print("space complexity-O(1)")

#for loop
a=11
for i in range(1,a):
    print(i)
print("jumping statements--------------------")
print("time complexity-O(n)")
print("space complexity-O(1)")

#Check given number is Prime or not
n=int(input("enter a number"))
prime=True
if n==0 or n==1:
    print("either prime nor composite")
elif n>1:
   for i in range(2,n):
     if n%i==0:
        prime=False
        break
   if prime:
    print("it is a prime number")
   else:
    print("not prime")
print("time complexity-O(n)")
print("space complexity-O(1)")

#Factorial of a given number
n=int(input("enter a number:"))
i=1
while n>0:
    i=i*n
    n=n-1
print(i)
print("time complexity-O(n)")
print("space complexity-O(1)")

#Number divisible by 3 and 5
n=int(input("enter a number:"))
if n==0:
    print("zero error")
for i in range(1,n+1):
    if i%3==0 or i%5==0:
        print(i)
print("time complexity-O(n)")
print("space complexity-O(1)")

#Reverse order program
n=int(input("enter a number:"))
temp=n
rev=0
sum=0
count=0
while temp>0:
    rem=temp%10
    rev=rev*10+rem
    temp=temp//10
    sum=sum+rem
    count+=1
print("reverse order of the given number:",rev)
print("sum of individual numbers in the given number",sum)
print("count of given number",count)
print("time complexity-O(log(n))")
print("space complexity-O(1)")

#print numbers from 1  to 100
n=int(input("enter a number"))
for i in range(1,n):
    print(i)
print("time complexity-O(n)")
print("space complexity-O(1)")

#sum of given numbers
n=int(input("enter values"))
sum=0
for i in range(1,n+1):
    sum=sum+i
print(sum)
print("time complexity-O(n)")
print("space complexity-O(1)")

#print even numbers
n=int(input("enter a number:"))
i=1
while i<=n:
    if i%2==0:
        print(i)
    i=i+1   
print("time complexity-O(n)")
print("space complexity-O(1)")

#To display multiplication table 
number = int(input("Enter a number: "))
if number==0:
    print("Anything * zero is zero")
else:
    for i in range(1, 21):  
        print(number,"x",i," =" ,number * i)
print("time complexity-O(1)")
print("space complexity-O(1)")
