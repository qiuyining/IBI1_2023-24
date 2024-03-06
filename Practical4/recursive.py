# Every number is two times the previous number plus three.
# This script is used to calculate the first five numbers when the first three members of this sequence are 4, 11, and 25.
# s means the number of the sequence. a means the numbers in this sequence. 
# Repeat calculating 5 times to get 5 numbers. 
s=1
a=0.5
while s<6:
    a=a*2+3
    s+=1
    print(a)