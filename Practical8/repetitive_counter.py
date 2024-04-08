seq = 'ATGCAATCGGTGTGTCTGTTCTGAGAGGGCCTAA'
import re
s=re.finditer(r'(?=(GTGTGT|GTCTGT))',seq)
count=0
for a in s:
    count+=1
print(count)