# Write a program that asks user their height (cm) and weight (kg), 
# and then calculate their BMI (Body Mass Index):
# BMI = mass (kg) / (height(m) x height(m) )
# Note: you must do the conversion from cm to m before calculation

# Then based on the BMI, tell them that they are:
# Severely underweight if BMI < 16
# Underweight if BMI is between 16 and 18.5
# Normal if BMI is between 18.5 and 25 
# Overweight if BMI is between 25 and 30
# Obese if BMI is more than 30

h = int(input("Your Height (cm): "))
w = int(input("Your Weight (kg)"))
bmi = w / (0.01*h*h)

if bmi < 16: 
    print ("Status: Severely underweight ") 
elif bmi >=16 and bmi <= 18.5:
    print ("Status: Underweight ")
elif bmi >= 18.5 and bmi <= 25:
    print ("Status: Normal")
elif bmi >= 25 and bmi <= 30:
    print("Status: Overweight")
elif bmi > 30:
    print ("Obese")


