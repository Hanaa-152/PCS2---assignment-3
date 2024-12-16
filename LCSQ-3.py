from Bio import SeqIO
from io import StringIO

def longest_common_subsequence(s, t):
    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if s[i - 1] == t[j - 1]:
            lcs.append(s[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return ''.join(reversed(lcs))

def solve_lcsq(file_content):
    sequences = [str(record.seq) for record in SeqIO.parse(StringIO(file_content), "fasta")]
    s, t = sequences[0], sequences[1]
    return longest_common_subsequence(s, t)

with open ("/Users/han3/Downloads/rosalind_lcsq-4.txt") as file:
    file_content = file.read()

print(solve_lcsq(file_content))
