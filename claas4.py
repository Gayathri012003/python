#REVERSE A STRING
#using for loop
a=str(input("enter a string:"))
b=""
for i in a:
    b=i+b
print(b)
#slice
print(a[::-1])
#using recursion
def rev_str(a):
    if len(a)==0:
        return a
    return a[-1] + rev_str(a[0:len(a)-1])
print(rev_str(a))



#reversing a list
list=[1,1,2]
low=0
high=len(list)-1
while low<high:
    list[low],list[high]=list[high],list[low]
    
print(list)

#input: a+((b-c)+d)  output:a+b-c+d
expression = "a+((b-c)+d)"
result = ""
i = 0

while i < len(expression):
    if expression[i] == '(' or expression[i] == ')':
        i += 1
        continue
    else:
        result += expression[i]
        i += 1

print(result) 





