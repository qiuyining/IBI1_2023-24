import blosum as bl

# Initialize BLOSUM62 matrix
matrix = bl.BLOSUM(62)

def read_fasta(filename):
    # Reads a single sequence from a FASTA file.
    with open(filename, 'r') as file:
        sequence = ''
        for line in file:
            if line.startswith('>'):
                continue  # Skip the header line that starts with '>'
            sequence += line.strip()  # Append each line of the sequence to the variable 'sequence'
        return sequence
    
# Function for Global Alignment
def global_alignment(seq1, seq2, scoring_matrix):
    # Perform a global alignment. Returns score and percentage identity.
    score = 0
    identical_count = 0
    for i in range(min(len(seq1), len(seq2))):
        score += scoring_matrix[seq1[i]][seq2[i]]  # Score for a match or mismatch
        if seq1[i] == seq2[i]:
            identical_count += 1
    percentage_identity = (identical_count / min(len(seq1), len(seq2))) * 100
    return score, percentage_identity

# Main Execution Script
seq1 = read_fasta('IBI_git/IBI1_2023-24/Practical13/SLC6A4_HUMAN.fa')
seq2 = read_fasta('IBI_git/IBI1_2023-24/Practical13/SLC6A4_MOUSE.fa')
seq3 = read_fasta('IBI_git/IBI1_2023-24/Practical13/SLC6A4_RAT.fa')

# Running alignments
score_hm, identity_hm = global_alignment(seq1, seq2, matrix)
score_hr, identity_hr = global_alignment(seq1, seq3, matrix)
score_mr, identity_mr = global_alignment(seq2, seq3, matrix)

print("Human-Mouse Alignment Score:", score_hm, "Percentage of identical amino acids :", identity_hm)
print("Human-Rat Alignment Score:", score_hr, "Percentage of identical amino acids :", identity_hr)
print("Mouse-Rat Alignment Score:", score_mr, "Percentage of identical amino acids :", identity_mr)