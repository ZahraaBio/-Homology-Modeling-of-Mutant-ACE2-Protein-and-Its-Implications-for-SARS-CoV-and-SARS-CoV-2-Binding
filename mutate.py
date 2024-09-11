def read_fasta(file_path):

    with open(file_path, 'r') as file:
        lines = file.readlines()

    header = lines[0].strip()
    sequence = ''.join(lines[1:]).replace('\n', '')
    return header, sequence

def modify_sequence(sequence, start_index, seq_length, n, new_char):

    if start_index < 0 or start_index + seq_length > len(sequence):
        raise IndexError("Sequence length and start index out of range")

    if n <= 0 or n > seq_length:
        raise IndexError("Nth character position out of range")

    index_to_modify = start_index + n - 1
    return sequence[:index_to_modify] + new_char + sequence[index_to_modify + 1:]

def write_fasta(file_path, header, sequence):
    """Writes the modified sequence to a FASTA file."""
    with open(file_path, 'w') as file:
        file.write(f"{header}\n")
        file.write('\n'.join([sequence[i:i+60] for i in range(0, len(sequence), 60)]))


input_fasta = "seq.fasta"  
output_fasta = "mseq1.fasta" 
start_index = 0  
seq_length = 805 
n = 31  
new_character = 'D'  


header, original_sequence = read_fasta(input_fasta)


modified_sequence = modify_sequence(original_sequence, start_index, seq_length, n, new_character)


write_fasta(output_fasta, header, modified_sequence)

print(f"Modified sequence written to {output_fasta}")
