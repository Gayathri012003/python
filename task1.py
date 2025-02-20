print(“Data Types------------------”)
    #integer
a=4
print(type(a),a)
   #float
b=3.5
print(type(b),b)
   #complex
b=2+3j
print(type(b),b)
   #string
c="hello"
print(type(c),c)
   #boolean
d=True
print(type(d),d)
   #list
d=[1,2,"hi",3]
print(type(d),d)
   #tuple
d=("hi",4,5,6)
print(type(d),d)
  #set
d={1,2,3}
print(type(d),d)
  #dictionary
d={1:"anu",2:"anji"}
print(type(d),d)
#range
e= range(10)
print(type(e),e)
print("Operators----------------------")
     #arithmetic Operators:
print(1+2)
print(5-2)
print(3*5)
print(9/3)
print(12 % 10)
print(2 ** 3)
print(16 // 4)
    #assignment Operators:
a= 10
print(a)
a= 10
a += 2
print(a)
a= 10
a-=2
print(a)
a = 10
a *= 2
print(a)
a = 10
a /= 4
print(a)
b = 10
b //= 2
print(b)
    #comparison Operators
a = 10
b = 5
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
     #logical Operators
a = 5
print(a>1 and a< 10)
print(a>1 or a<10)
print(not(a>1 and a<10))
   #bitwise Operators
print(2 & 3)
print( 10 | 2)
print(~5)
print(3 << 2)
print(8 >> 2)
print("conditional statements---------------------")
#if condition
a=5
if a>0:
    print("a is positive")
#else condition
a=5
if a<0:
    print("a is negative")
else:
    print("a is positive")
#elif
a=-10
if a==0:
    print("a is zero")
elif a>0:
    print("a is positive")
else:
    print("a is negative")
print("looping statements--------------------")
#while loop
a=1
while a<6:
    print(a)
    a=a+1
#for loop
a=11
for i in range(1,a):
    print(i)
print("jumping statements--------------------")
#break
a=1
while a<6:
    print(a)
    a=a+1
    if a==4:
        break
#continue
a=11
for i in range(1,a):
    if i==4:
        continue
    else:
        print(i)
#pass
for i in range(1,a):
    pass
print("functions-------------")
#define a function and calling a function
def mul(a,b):
    print(a*b)
mul(2,3)  #calling a function
#define a function using return and calling
def mul(a,b):
    return a*b
print(mul(4,5)) # calling a function
print("In-Built Functions------------------")
#list methods
list = [1, 2, 3]
print(list)
list.append(4)
print(list)
list.extend((5,6,7))
print(list)
list.remove(2)
print(list)
list.pop()
print(list)
list.clear()
print(list)
#string methods
string="hello"
print(len(string))
print(string.find("e"))
str1="name"
print(string+" "+str1) #concate with space
print(string.upper())
print(string.lower())
print(string.capitalize())
print(string.split())
print(string[1:3])
print(string[2])
