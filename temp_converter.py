# This programe is covert the temperature from 
# celcius to farenheit and vice versa
# This program takes a numerical value and converts it based on user selection.

Temp=int(input("enter the temperature you want to convert:"))
choice=input("convert it in celcius or farenheit:").lower()
if (choice=="c" or choice=="celcius"):
    celcius=(Temp-32)*5/9
    print("the temperature is:",celcius,"celcius")
elif (choice=="f" or choice=="farenheit"):
    farenheit=(Temp*9/5)+32
    print("the temprature is :",farenheit,"farenheit")
else:
    print("error invalid choice")