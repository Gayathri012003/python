list=eval(input("enter nested list:")) #input:[[21,31],[33,45]]
def sum_of_list(num):
        temp=num
        sum=0
        while temp>0:
            digit=temp%10
            temp=temp//10
            sum=sum+digit
        return sum

def nested_list(list):
    result_list=[]
    for i in list:
        l1=[]
        for sublist in i:
            l1.append(sum_of_list(sublist))
        result_list.append(l1) 
    return (result_list)
print(nested_list(list),"sum of a number in a nested list")   #output:[[3, 4], [6, 9]]


def nested_min_max(list):
    max=[]
    min=[]
    largest=0
    
    for i in list:
        for sublist in i:
            if sublist>largest:
                largest=sublist
        max.append(largest)
        smallest=largest
        for sub in i:
            if sub < smallest:
                smallest=sub
        min.append(smallest)
    
    print(max,"maximum numbers in nested list")
    print(min,"minimum numbers in nested list")
nested_min_max(list)
        

