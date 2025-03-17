#matrix
list=[[2,5,3,4],[4,7,1,5],[3,0,5,8]]
sum=0
for i in list:
    for j in i:
        sum+=j
print(sum)
for i in list:
    print(i)
    break
for i in range(0,len(list)):
    for j in range(0,len(list[i])):
        print(list[i][j],end=" ")
    print()
for i in range(0,len(list)):
    for j in range(0,len(list[i])):
        if i==0:
           print(list[i][j],end=" ")
    print()
for i in range(0,len(list)):
    for j in range(0,len(list[i])):
        if j==0:
            print(list[i][j],end=" ")
    print()
n=len(list)
for i in range(0,len(list)):
    for j in range(0,len(list[i])):
        if  i==0 or j==0 or i==n-1 or j==len(list[i])-1:
            print(list[i][j],end=" ")
        else:
            print(" ",end=" ")
    print() 
sum=0
for i in range(0,len(list)):
    for j in range(0,len(list[i])):
        if  i==0 or j==0 or i==n-1 or j==len(list[i])-1:
            print(list[i][j],end=" ")
            sum+=list[i][j]
        else:
            print(" ",end=" ")
    print()
print(sum)


sum=0
for i in range(0,len(list)):
    for j in range(0,len(list[i])):
        if i==j:
             print(list[i][j],end=" ")
             sum+=list[i][j]
        elif i+j==len(list)-1:
            print(list[i][j],end=" ")
        else:
            print(" ",end=" ")
    print( )
print("\n",sum)


list=[[1,2],[4,5]]
list2=[[1,3],[6,1]]
for i in range(len(list)):
    for j in range(len(list[i])):
        print(list[i][j]+list2[i][j],end=" ")
    print( )

matrix1 = [[1, 2, 3],[4,5,6]]
matrix2 = [[7, 8], [9, 10], [11, 12]]

rows1 = len(matrix1)
cols1 = len(matrix1[0]) if rows1 > 0 else 0
rows2 = len(matrix2)
cols2 = len(matrix2[0]) if rows2 > 0 else 0

if cols1 != rows2:
    print("Matrices cannot be multiplied.")
else:
    result = [[0 for _ in range(cols2)] for _ in range(rows1)]

    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    for row in result:
        print(row)
