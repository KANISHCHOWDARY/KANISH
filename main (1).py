m=1
n=int(input("Enter the number :"))
for i in range(1,11):
    m=i*n
    print(n,"X",i,"=",m)
w=float(input("Enter the weight  :"))
h=float(input("Enter the height  :"))
bmi=w/(h**2)
if bmi<18.5:
    print("underweight")
elif (bmi>=18.5) and (bmi<=24.9):
    print("Normalweight")
elif (bmi>=25) and (bmi<=29.9):
    print("overweight")
else:
    print("obesity")
print("Your BMI is ",bmi)   
    
    
    
    
    


    



    



