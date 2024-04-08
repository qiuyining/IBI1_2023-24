input='D:/IBI/IBI_git/IBI1_2023-24/Practical8/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
output='D:/IBI/IBI_git/IBI1_2023-24/Practical8/duplicate_genes.fa'

input_file = open(input, 'r')
output_file = open(output, 'w')

record_sequence = False

for line in input_file:
    if line.startswith('>'):
        if 'duplication' in line:
            gene_name = line.split()[0][1:]
            output_file.write(f'>{gene_name}\n')
            record_sequence = True
        else:
            record_sequence = False
    else:
        if record_sequence:
            output_file.write(line)

input_file.close()
output_file.close()
                  