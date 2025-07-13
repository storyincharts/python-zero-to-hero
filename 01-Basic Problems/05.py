## Converting Temperature Units
# Input = temperature_celsius = 30
# output = temperature in Fahrenheit: 86.0, and Temperature in Kelvin:303.15
# Consider Celsius = c, fahrenheit =f, and k = kelvin

c = int(input("Celcius:"))
f = c * (9/5) + 32
k = 273.15 + c

print(f"Fahrenheit:{f},Kelvin:{k}",sep=",")