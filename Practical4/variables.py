a=40
b=36
c=30
d=a-b
e=b-c
if d>e:
    print("d is greater. Running had a greater improvement on running time.")
elif d<e:
    print("e is greater. The combination of running and strength exercises had a greater improvement on running time.")
else:
    print("d is as great as e. Two training regime had the same improvement on running time")

# e is greater than d.The combination of running and strength exercises had a greater improvement on running time.
    
X=True
Y=False
W=not (X and Y) and (X or Y)
print(W)

# Z is true.
# truth table:
# X    Y     W
#True  True  False
#True  False True
#False True  True
#False False False

