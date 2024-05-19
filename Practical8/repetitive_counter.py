# Define the sequence
seq = 'ATGCAATCGGTGTGTCTGTTCTGAGAGGGCCTAA'
# import necessary library
import re
# find all occurrences of GTGTGT or GTCTGT in the sequence
s=re.finditer(r'(?=(GTGTGT|GTCTGT))',seq)
# Initialize a counter to zero
count=0
# Go through each found pattern
for matched_element in s:
    # Add one to the count for each pattern found
    count+=1
# Print the total count
print(count)
