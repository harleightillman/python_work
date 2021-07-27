#Ask question to be answered
print("How many kilometers did you travel today?")

#take users input and assign input to kms variable
kms = input()

#convert kms to miles through division
miles=float(kms)/1.60934

#round to two decilmal places
miles = round(miles, 2)

#pring result using f strings to input input and result
print(f"Your {kms} km trip converts to {miles} miles.")



