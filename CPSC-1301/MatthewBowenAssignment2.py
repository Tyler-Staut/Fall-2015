# Purpose: This program calculates and displays the wind 
# chill temperature index for given temperatures and wind 
# speed
# Author(s): Matthew Newton Bowen
# Date: 11 September 2015

print("Examples:")

print("----------------------------------------")

airTemp = float(10)

airSpeed = float(15)

wctIndex = 35.74 + 0.6215 * airTemp - 35.75 * airSpeed ** (0.16) + 0.4275 * airTemp * airSpeed ** (0.16)

print("Temperature in Degrees F: ", airTemp)
print("Wind Speed in MPH: ", airSpeed)
print("Wind Chill Temperature Index: ", wctIndex, "\n")

airTemp = float(0)

airSpeed = float(25)

wctIndex = 35.74 + 0.6215 * airTemp - 35.75 * airSpeed ** (0.16) + 0.4275 * airTemp * airSpeed ** (0.16)

print("Temperature in Degrees F: ", airTemp)
print("Wind Speed in MPH: ", airSpeed)
print("Wind Chill Temperature Index: ", wctIndex, "\n")

airTemp = float(-10)

airSpeed = float(35)

wctIndex = 35.74 + 0.6215 * airTemp - 35.75 * airSpeed ** (0.16) + 0.4275 * airTemp * airSpeed ** (0.16)

print("Temperature in Degrees F: ", airTemp)
print("Wind Speed in MPH: ", airSpeed)
print("Wind Chill Temperature Index: ", wctIndex, "\n")
print("----------------------------------------")


airTemp = float(input("Temperature in Degrees F: "))

airSpeed = float(input("Wind Speed in MPH: "))

wctIndex = 35.74 + 0.6215 * airTemp - 35.75 * airSpeed ** (0.16) + 0.4275 * airTemp * airSpeed ** (0.16)

print("Wind Chill Temperature Index: ", wctIndex)
