repetitive_sequence = input('Input one of the two repetitive sequences GTGTGT or GTCTGT: ') 
input_path = 'D:/IBI/IBI_git/IBI1_2023-24/Practical8/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
output_path = f'D:/IBI/IBI_git/IBI1_2023-24/Practical8/{repetitive_sequence}_duplicate_genes.fa'
input_file = open(input_path, 'r')
output_file = open(output_path, 'w')
gene_name = ""
gene_sequence = ""

for line in input_file:
    if line.startswith('>'):
        if gene_name and repetitive_sequence in gene_sequence:
            repeat_count = gene_sequence.count(repetitive_sequence)
            output_file.write(f">{gene_name} {repeat_count}\n")
               
        gene_name = line.strip().split()[0][1:]  
        
        gene_sequence = ""
    else:
        gene_sequence += line.strip()

input_file.close()
output_file.close()