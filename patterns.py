#patterns
'''output:
enter a number:5
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 

x=int(input("enter a num:"))
for i in range(x):
    for j in range(x):
        print("*",end=" ")
    print( )
'''  
'''
output:
enter a number:5
x x x x x 
  x x x x 
    x x x 
      x x 
        x     
x=int(input("enter a num:"))
for i in range(x):
    for j in range(x):
        if i<=j:
            print("x",end=" ")
        else:
            print(" ",end=" ")
    print()'''
'''output:
enter a number:5
*         
* *       
* * *     
* * * *   
* * * * * 
n=int(input("enter a number:"))
for i in range(n):
    for j in range(n):
        if i>=j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''
'''output:
enter a number:5
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*    

n=int(input("enter a number:"))
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()
for i in range(n):
    for j in range(n-1-i):
            print("*",end=" ")
    print( )'''

'''output:
enter a number:5
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 

n=int(input("enter a number:"))
for i in range(n):
    for j in range(i+1):
        print(j+1,end=" ")
    print()
for i in range(n):
    for k in range(n-1-i):
        print(k+1,end=" ")
    print()'''
'''
output:
enter a number:5
*       * 
  *   *   
    *     
  *   *   
*       * 
n=int(input("enter a number:"))
for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
'''
'''output:
enter a number:5
* * * * * 
*       * 
*       * 
*       * 
* * * * * 
n=int(input("enter a number:"))
for i in range(n):
    for j in range(n):
        if  i==0 or j==0 or j==n-1 or i==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''
'''output:
enter a number8
* * * * * * * * 
* *         * * 
*   *     *   * 
*     * *     * 
*     * *     * 
*   *     *   * 
* *         * * 
* * * * * * * * 
n=int(input("enter a number"))
for i in range(n):
    for j in range(n):
            if i==0 or j==0 or j==n-1 or i==n-1 or i==j  or i+j==n-1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
    print( )'''

'''enter a num5
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
n=int(input("enter a num"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
'''
'''enter a number:5
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15
num=int(input("enter a number:"))
count=1
for i in range(num):
    for j in range(num):
        if i>=j:
            print(count,end=" ")
            count+=1
    print()
 
 enter a number:5
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
    
num=int(input("enter a number:"))
for i in range(num):
    for k in range(1,num-i):
        print(" ",end="")
    for j in range(num):
        if i>=j:
            print("*",end=" ")
    print()
'''
