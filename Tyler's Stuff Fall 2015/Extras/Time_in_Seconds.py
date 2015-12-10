#Author: Tyler R. Staut
#File Name: Time in Seconds
#Date: 9/4/2015
#Description: Converts time in seconds to hours and min.

#------------------------INTRO------------------------------------------------------------
print("This will take your time and Seconds and convert it into hours and min.\n")
#-----------------------------------------------------------------------------------------

#------------------------INPUT------------------------------------------------------------
seconds = int(input("Time in Seconds: "))
#-----------------------------------------------------------------------------------------

#------------------------CACULATIONS------------------------------------------------------
minutes = (seconds // 60) % 60
hours = (seconds // 3600)
remaning_seconds = seconds % 60
#-----------------------------------------------------------------------------------------

#------------------------OUPUT------------------------------------------------------------
print(seconds, 'Seconds is equivalent to', hours,
      "Hours", minutes, "Minutes and", remaning_seconds, "Seconds")
#-----------------------------------------------------------------------------------------

