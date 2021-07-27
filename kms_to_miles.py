#asks question to be answered 
print("How many kilometers did you travel today?")

#take users input and assign input to kms variable
kms = input()

#Convert kms to miles through division and assign to variable miles
miles = (int(kms))/1.60934

#round miles to two decimal places and assign to variable miles_round
miles_round = round(miles,2)

#turn miles_round back into a string and assign to variable result
result = str(miles_round)

#print out result using f string variable
print(f"Your {kms} km trip converts to {result} miles.")
