def printer(n):
    if n==0:
        return 0
    return n+printer(n-1)
    
print(printer(10))

def printer1(n):
    if n==1:
        return
    printer1(n-1)
    print(n)
printer1(10)

 
def fibonoci(nterms):
    if nterms<=1:
         return nterms
    return (fibonoci(nterms-1)+fibonoci(nterms-2))
print(fibonoci(10))

def exponent(n,m):
    if m<=1:
        return n
    return (n*exponent(n,(m-1)))
n=int(input("enter base value"))
m=int(input("enter power num"))
print(exponent(n,m))


def check_palindrome(input_str):
    if len(input_str)<=1:
        return True
    return input_str[0]==input_str[-1] and check_palindrome(input_str[1:-1])
print(check_palindrome("madam"))

