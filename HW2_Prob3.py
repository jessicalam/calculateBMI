#This program is supposed to take in the kilograms and height of a person and calculate it's body mass index.
#We calculated the body mass index is taking the weight and dividing it by the height squared.
#This program is written by Jessica Lam and Kevin Kye.
#Date Completed: Sepetember 21, 2017

#initiated values
weight= int(input("Tell me your weight in kilograms:"))
height=float(input("Tell me your height in meters:"))

#calculation part, split up to two operations. For easier visuals.
height_squared = float(height*height)
body_mass_index= int(weight) / height_squared

print("For", weight,"kg,", height, "m, Your BMI is", body_mass_index)
