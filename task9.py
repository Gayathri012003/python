#addition of two matries
list=[[1,2,5],[4,5,6]]
list2=[[1,3,1],[6,1,8]]
for i in range(len(list)):
    for j in range(len(list[i])):
        print(list[i][j]+list2[i][j],end=" ")
    print( )
    

#diagnols of matrix
l=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(0,len(l)):
    for j in range(0,len(l[i])):
        if i==j or i+j==len(l)-1:
           print(l[i][j],end=" ")
        else:
            print(" ",end=" ")
    print( )
