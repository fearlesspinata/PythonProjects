#!/usr/bin/env python3.6

# BMI = (weight in kg / height in meters squared)
# Imperial BMI * 703
def getInfo():
    weight = float(input("What is your weight (in pounds or kilograms)?: " ))
    height = float(input("What is your height (in inches or meters)?: "))
    system = input("Are you measurements in metric or imperial units?: ").lower().strip()
    return (weight, height, system)

def calculate(weight, height, system):
    if system == "metric":
        BMI = weight / height ** 2
    elif system == "imperial":
        BMI = 703 * (weight / height ** 2)
    return BMI

while True:
    weight, height, system = getInfo()
    if system.startswith('i'):
        BMI = calculate(weight, height, system='imperial')
        print(f"Your BMI is {BMI}")
        break
    elif system.startswith('m'):
        BMI = calculate(weight, height, system='metric')
        print(f"Your BMI is {BMI}")
        break
    else:
        print("Please select a valid measurement system.")

