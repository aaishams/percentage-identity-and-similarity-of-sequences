def n_seq(seq1, seq2):
    s = 0
    for i, j in zip(seq1, seq2):
        if i == j and i != '-' and j != '-':
            s += 1
        else:
            continue
    similarity = (s / len(seq1)) * 100
    return similarity

def p_seq(seq1, seq2):
    id = 0
    s = 0
    for i, j in zip(seq1, seq2):
        if i == j and i != '-' and j != '-':
            id += 1
        elif i != '-' and j != '-':
            s += 1
        else:
            continue
    identity = (id / len(seq1)) * 100
    similarity = ((id + s) / len(seq1)) * 100
    return identity, similarity

while True:    
    type_of_seq = input("For nucleotide sequences, enter 'N' and for protein sequences, enter 'P':")
    type_of_seq = type_of_seq.upper()
    if type_of_seq in ['N', 'P']:
        break
    else:
        print("Invalid input! Please enter the letter corresponding to your type of sequence.")

while True:
    seq1 = input("Enter the first sequence:")
    seq2 = input("Enter the second sequence:")
    seq1 = seq1.upper()
    seq2 = seq2.upper()
    if len(seq1) == len(seq2):
        break
    else:
        print("Please enter sequences of equal length!")

if type_of_seq == 'N':
    similarity = n_seq(seq1, seq2)
    print("The percentage similarity =", similarity, "%")
elif type_of_seq == 'P':
    identity, similarity = p_seq(seq1, seq2)
    print("The percentage identity =", identity, "%")
    print("The percentage similarity =", similarity, "%")