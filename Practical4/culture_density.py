# a means the initial density percentage of the cell line. d means the number of days the cell line grows. 
# The cell doubles every day.
# While the density percentage is under 90%, I can leave the lab.
# Until the density percentage passes 90%, I should come back.
# The day the cell density goes over 90% is the maximum number of days I can have a holiday from the lab.
# while allows the density percentage doubles and calculating days until the density percentage passes 90%
a=5
d=0
while a<=90:
    a=a*2
    d+=1
    if a>90:
     print("The maximum number of days I can have a holiday from the lab is", str(d))