#1largest of three numbers
a=int(input("enter a number:"))
b=int(input("enter a number:"))
c=int(input("enter a number:"))
if a>b:
    if a>c:
        print("a is big")
    else:
        print("c is big")
elif b>c:
    print("b is big")
else:
    print("c is big")
#2leap year
year=int(input("enter year:"))
if (year%4==0 and year%100!=0) or year%400==0:
            print("leap year")
else:
        print("not leap year")
#3vowels
char=str(input("Enter the letter:"))
if char.lower() in "aeiou":
    print(char,"is vowel")
else:
    try:
        int(char) 
        print("invalid") 
    except ValueError:
        print(char, "is consonant")
#4Grade
Grade=int(input("enter grade of the student:"))
if Grade>100:
    print("not defined")
elif Grade>=90 and Grade<=100:
    print("Grade A")
elif Grade>=80 and Grade<=89:
    print("Grade B")
elif Grade>=70 and Grade<=79:
    print("Grade C")
else:
    print("Fail")
#5to check given numbers form valid triangle or not
a=int(input("enter a number:"))
b=int(input("enter a number:"))
c=int(input("enter a number:"))
if a+c>b and a+b>c and b+c>a:
    print("valid triangle")
else:
    print("not valid")
