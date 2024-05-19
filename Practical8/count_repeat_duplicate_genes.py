# Ask the user to input sequence
repetitive_sequence = input('Input one of the two repetitive sequences GTGTGT or GTCTGT: ') 
# Check the input 
if repetitive_sequence not in ['GTGTGT','GTCTGT']:
    print('please input GTGTGT or GTCTGT')
    exit()
input_path = 'D:/IBI/IBI_git/IBI1_2023-24/Practical8/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
output_path = f'D:/IBI/IBI_git/IBI1_2023-24/Practical8/{repetitive_sequence}_duplicate_genes.fa'
# Open the input and output file
input_file = open(input_path, 'r')
output_file = open(output_path, 'w')
# Initialize variables to store the gene name and sequence
gene_name = ""
gene_sequence = ""

 # Read the input file line by line
for line in input_file:
    if line.startswith('>'):
        if gene_name and repetitive_sequence in gene_sequence:
            # Count how many times the repetitive sequence occurs in the gene sequence
            repeat_count = gene_sequence.count(repetitive_sequence)
            # Write the gene name, repeat count, and sequence to the output file
            output_file.write(f">{gene_name} {repeat_count}\n{gene_sequence}\n")
         # Extract the gene name from the line
        gene_name = line.strip().split()[0][1:]  
         # Reset the gene sequence for the next gene
        gene_sequence = ""
      # If the line is not a gene name, add it to the gene sequence
    else:
        gene_sequence += line.strip()
    
# Close the input file
input_file.close()
output_file.close()
