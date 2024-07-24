# Convert minutes to hours.
# Start with a variable that contains the number of minutes to be converted.
# Take that number, do some calculation, and print the result
# The result format should be as follows: # minutes = 123
# Hours
# 2
# Minutes
# 1

# "60 Minutes" is converted to "1 Hour and 0 Minutes"
# "95 Minutes" is converted to "1 Hour and 35 Minutes"
# "175 Minutes" is converted to "2 Hours and 55 Minutes"

# User input of Minutes
minutes = input("How many minutes do you want to convert? ")
minutes_to_convert = int(minutes) # converts the input to integer

# Calculations
hours_decimal = minutes_to_convert / 60
hours_part = int(hours_decimal)

minutes_part = minutes_to_convert % 60 # gives only the remainder of the division

# Need to convert results to a string for the printing option I used below
# (Textbook used separate print commands for each element.)

# Output
print("Hours\n" + str(hours_part))
print("Minutes\n" + str(minutes_part))

print("\n~~~~~~~~~~\n")

# Write a program that initializes a variable with the value of 75 to represent the 
# temperature in Fahrenheit. Then convert that value to Celsius by using the formula 
# c = (f - 32) / 1.8. Print the Celsius value.
temp = input("What temperature (F) would you like to convert to C?\nWhole number, please... ")
f = int(temp)
c = (f - 32) / 1.8
print("The Celsius temperature is %s." % round(c, 2))

print("\n~~~~~~~~\n")

distance = input("Enter the miles to convert to kilometers: ")
miles = float(distance)
km = round(miles / 0.62137, 2)
meters = 1000 * km

print("Miles\n" + str(miles))
print("Kilometers\n" + str(km))
print("Meters\n" + str(meters))

print("\n~~~~~~~~\n")

# mandi628 2024.07.08
