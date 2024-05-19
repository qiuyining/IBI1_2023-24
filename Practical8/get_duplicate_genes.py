# Define the path to the input and output file
input='D:/IBI/IBI_git/IBI1_2023-24/Practical8/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
output='D:/IBI/IBI_git/IBI1_2023-24/Practical8/duplicate_genes.fa'

# Open the input file for reading
input_file = open(input, 'r')
# Open the output file for writing
output_file = open(output, 'w')

record_sequence = False

# Read the input file line by line
for line in input_file:
     # Check if the line starts with '>', indicating a gene name line
    if line.startswith('>'):
        # Check if 'duplication' is in the line
        if 'duplication' in line:
            # Extract the gene name
            gene_name = line.split()[0][1:]
            # Write the gene name to the output file
            output_file.write(f'>{gene_name}\n')
            # start recording the sequence
            record_sequence = True
        # If 'duplication' is not in the line, stop recording
        else:
            record_sequence = False
    else:
        if record_sequence:
            # Write the current line (part of the gene's sequence) to the output file
            output_file.write(line)

# Close the input and output file
input_file.close()
output_file.close()
                  
