'''
#swapping of two numbers using third variable
a=10
b=1
temp=a
a=b
b=temp
print(a)
print(b)


#swapping of two numbers using add,sub
x=10
y=5
x=x+y
y=x-y
x=x-y
print(x,y)

#swapping of two numbers 
x=10
y=2
x,y=y,x
print(x,y)


#swapping of two numbers using mul,div
x=9
y=8
x=x*y
y=x//y
x=x//y
print(x,y)

#swapping of two numbers using xor
a=10
b=20
a=a^b
b=a^b
a=a^b
print(a,b)
#swapping of two numbers using xor and sub
a=10
b=20
a=a^b
b=a-b
a=a-b
print(a,b)

'''
'''#check if list is in sorted order or not
x=[1,2,3,4,5]
flag=True
for i in range(0,len(x)-1):
    if x[i]>x[i+1]:
        flag=False
        print("false")
        break
if flag ==True:
    print("true")


def asc_sorted(x):
    for i in range(len(x)-1):
        if x[i]>x[i+1]:
            return "false"
    return "true"
def dec_sorted(x):
    for i in range(len(x)-1):
        if x[i]<x[i+1]:
            return "false"
    return "true"
    
def is_sorted(x):
    return asc_sorted(x) or dec_sorted(x)
print(is_sorted(x))
        
'''

    
        
        
    
