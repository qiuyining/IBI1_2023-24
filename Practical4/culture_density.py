# a means the initial density percentage of the cell line. d means the number of days the cell line grows. 
# The cell doubles every day.
a=5
d=0
while a<=90:
    a=a*2
    d+=1
    if a>90:
        print("The maximum number of days I can have a holiday from the lab is", str(d-1))
#The density reaches 80% at the end of the forth day, and 90% and exceeds during the fifth day.
#So I can only leave the laboratory for a maximum of 4 days.
