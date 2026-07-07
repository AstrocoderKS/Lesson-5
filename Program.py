#Rohan wants to build a wearing weather-appropriate clothes program.
# Temperature is measured in °C
A = int(input("Enter your randomly chosen temperature."))
if A <= 10:
    print("Wear pants, a jacket and sweater. But if the temperature is way below -10, wear a beanie, and thicker winter clothes.")
else:
    print("Wear pants and a jacket, but if just right or warm, wear just a shirt, and shorts to maintain temperature in the human body.")