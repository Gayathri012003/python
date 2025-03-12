num=int(input("enter a number:"))
temp=num
list=[]
while temp>0:
    digit=temp%10
    temp=temp//10
    list.append(digit)
list_max=max(list)
list_min=min(list)
print(list_max)
print(list_min)

print(list)
flag=True
for i in range(list_min,list_max):
    if i not in list:
        flag=False
        print(i,"missing")
if flag==True:
    print("no missing numbers")
