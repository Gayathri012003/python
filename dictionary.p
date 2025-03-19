list=eval(input("enter array"))
count={}
for i in list:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print(count)
max=0
max_key=" "
for i,j in count.items():
    print(i,":",j)
    if j>max:
        max=j
        max_key=i
if max!=0:
      print(max_key)
else:
    print("dictionary is empty")
for i,j in count.items():
    if j>1:
        print(i,":",j)
dict1={}
for i,j in list.items():
    if j in dict1:
        dict1[j].append(i)
    else:
        dict1[j]=[i]
        
print(dict1)

#find if 2 strings are anagrams
s1=str(input("enter s1:"))
s2=str(input("enter s1:"))
count={}
count1={}
if len(s1)!=len(s2):
    print("false")
else:
  for i in s1:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
  for j in s2:
    if j in count1:
        count1[j]+=1
    else:
        count1[j]=1
  print(count)
  print(count1)
  if count==count1:
    print("true")
  else:
    print("false")





d1={1:4,2:5}
d2={1:3,2:3,3:6}
od={}
for i,j in d1.items():
    od[i]=j
for i,j in d2.items():
    if i in od:
        od[i]+=j
    else:
        od[i]=j
        
print(od)

