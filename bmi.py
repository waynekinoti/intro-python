#BMI calc
weight=73.4
height=1.78
bmi=weight/height**2
if bmi < 18.5:
    print("underweight")
elif bmi >= 18.5 and bmi <= 24.9:
    print("normal")
elif bmi >= 25 and bmi <= 29.9:
    print("overweight")
elif bmi >= 30 and bmi <= 34.9:
    print("obese")
elif bmi >= 35 and bmi <= 39.9:
    print("Severely obese")
else:
    print("Morbidly Obese")