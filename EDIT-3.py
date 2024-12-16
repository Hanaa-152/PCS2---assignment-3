from Bio import SeqIO
from io import StringIO

def edit_distance(s, t):
    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

    return dp[m][n]

def solve_edit(file_content):
    sequences = [str(record.seq) for record in SeqIO.parse(StringIO(file_content), "fasta")]
    s, t = sequences[0], sequences[1]
    return edit_distance(s, t)

with open("/Users/han3/Downloads/rosalind_edit.txt") as file:
    file_content = file.read()

print(solve_edit(file_content))
