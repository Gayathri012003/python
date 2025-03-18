#sum of a digit
def digit_sum(num):
    if num<=0:
        return 0
    return (num%10) + digit_sum(num//10)
num=543
print(digit_sum(num))

#reverse a string
def str_rev(str1):
    if len(str1)<=0:
        return str1
    return str1[-1]+str_rev(str1[0:-1])
str1=str(input("enter a string"))
print(str_rev(str1))

#Reverse order of list
def rev_list(list1):
    if len(list1)==0:
       return []
    return [list1[-1]]+rev_list(list1[0:-1])
list1=eval(input("enter a list"))
print(rev_list(list1))

#Maximum number in a list using recursion

def max_of_list(l):
    if len(l)==0:
         return "no maximum"
    if len(l)==1:
        return l[0]
    rem_max =max_of_list(l[1: ])
    return l[0] if l[0]>rem_max else rem_max
print(max_of_list(list1))
    
