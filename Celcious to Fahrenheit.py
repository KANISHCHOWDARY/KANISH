
#Write a function celsius_to_fahrenheit(celsius) that converts a temperature from Celsius to Fahrenheit. Test the function with the user given input


def celsius_to_fahrenheit(c):
    c=((c*(9/5))+32)
    print("Temperature in fahrenheit is ", c)
    
c=int(input("Enter the temperature in celcious :"))
celsius_to_fahrenheit(c)



    
