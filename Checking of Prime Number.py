num=int(input("Enter the number :"))

def prime_number(num):
    if num<=1:
        return False
        
    for i in range (2,num):
        if num%i==0:
            return False
    return True
    
if  prime_number(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
    
    

        
        
















