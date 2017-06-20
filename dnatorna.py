"""
Convert DNA sequences to RNA.
"""
def rna(seq):
    """Convert DNA sequence to RNA sequence."""

    #Determine is original sequence was uppercase
    seq_upper = seq.isupper()

    #Convert the sequence to lowercase
    seq = seq.lower()

    #Swap out 't' for 'u'
    seq = seq.replace('t', 'u')

    #Return upper or lower, depending on input
    if seq_upper:
            return seq.upper()
    else:
        return seq

def reverse_rna_complement(seq):
    """Convert DNA sequence into it's reverse complement as RNA"""

    #Determine is original sequence was uppercase
    seq_upper = seq.isupper()

    #Reverse the sequence
    seq = seq[::-1]

    #Convert to uppercase
    seq = seq.upper()

    #Compute complement
    seq = seq.replace('A', 'u')
    seq = seq.replace('T', 'a')
    seq = seq.replace('G', 'c')
    seq = seq.replace('C', 'g')

    #Return in appropriate case
    if seq_upper:
        return seq.upper()
    else:
        return seq
