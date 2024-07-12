k=[]
while True:
    c=input(("Enter the value :"))
    if c=="done":
        break
    k.append(c)
print(k)
def feet():
    print("Bye world")
    
feet()
d=input("Enter the name :")
def greet(d):
    print("Hello",d) 

greet(d)
def sum(a,b):
    c=a*b
    print(c)
    
g=int(input("Enter the number 1 :"))
h=int(input("Enter the number 2 :"))
sum(g,h)

sum(23,78)
def eveodd(i):
    if i%2==0:
        print("given number is even")
    else:
        print("given number is odd")
        
i=int(input("Enter the number :"))
eveodd(i)
def fact(fa):
    for i in range(1,fa+1):
        fa*=i
    print(fa)
fa=int(input("Enter the number :"))
fact(fa)
print("factorial of ","=", fa)
def find_max(a,b,c):
    if a > b and a > c:
        return a
        
    elif b > a and b > c:
        return b
        
    else:
        return c
        
a=int(input("Enter the number1"))
b=int(input("Enter the number2"))
c=int(input("Enter the number3"))
print("Maximum of",a,b,c,"is",find_max(a,b,c))



        
        
        
        
        
        
        
    
    
        
     
    
        
        

















































































