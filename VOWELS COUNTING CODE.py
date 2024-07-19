sum=0
n=input("Enter the string :")
vowels="aeiouAEIOU"
for i in n:
    if i in vowels:
        sum+=1 
    
print("Count of vowels is :",sum)    