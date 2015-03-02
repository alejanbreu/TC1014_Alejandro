print ("Temperature")

F = int(input("Fahrenheit"))
C = 5*(F-32)/9

print ("Celsius", C)

if C>=100:
    print("Water boils at this temperature (under typical conditions)")

else:
    print("Water does not boil at this temperature (under typical conditions)")
