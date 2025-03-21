#find the largest word in a string
   #input:"google doc is better"   output:google 
input_string = str(input("enter a string")).split()
if not input_string:
    largest_word = ""
else:
    largest_word = input_string[0]  
    max_length = len(input_string[0])

    for word in input_string:
        if len(word)> max_length:
            max_length = len(word)
            largest_word = word
print(largest_word)


str1=str(input("enter a string"))
word_list=str1.split()
print(word_list)


max_string=word_list[0]
max_elem_list=[]
for i in word_list:
    if len(i)>len(max_string):
        max_elem_list.clear()
        max_elem_list.append(i)
        max_string=i
    elif len(i)==len(max_string):
        max_elem_list.append(i)
print(max_elem_list)


string1=str(input("enter a string"))
list=[]
for i in range(len(string1)):
    for j in range(i+1,len(string1)+1):
        list.append(string1[i:j])
print(list)
for i in range(len(list)):
    b=""
    for j in list[i]:
        b=j+b
    if list[i]==b:
        print("palindrome",list[i])
    
        
