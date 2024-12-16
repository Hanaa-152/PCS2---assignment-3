from Bio import SeqIO
from io import StringIO

def subseq_pos(file_content):
    file_like_object = StringIO(file_content)
    s, t = [str(record.seq) for record in SeqIO.parse(file_like_object, "fasta")]
    
    positions = []
    t_index = 0
    
    for i, char in enumerate(s):
        if t_index < len(t) and char == t[t_index]:
            positions.append(i + 1)
            t_index += 1
        if t_index == len(t):
            break

    return positions

with open ("/Users/han3/Downloads/rosalind_sseq-3.txt") as file:
    file_content = file.read()

print(" ".join(str(pos) for pos in subseq_pos(file_content)))
