from Bio import SeqIO
from io import StringIO

def edta(s, t):
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

    aligned_s = []
    aligned_t = []
    i, j = m, n

    while i > 0 or j > 0:
        if i > 0 and j > 0 and (s[i - 1] == t[j - 1] or dp[i][j] == dp[i - 1][j - 1] + 1):
            aligned_s.append(s[i - 1])
            aligned_t.append(t[j - 1])
            i -= 1
            j -= 1
        elif i > 0 and dp[i][j] == dp[i - 1][j] + 1:
            aligned_s.append(s[i - 1])
            aligned_t.append('-')
            i -= 1
        else:
            aligned_s.append('-')
            aligned_t.append(t[j - 1])
            j -= 1

    return dp[m][n], ''.join(reversed(aligned_s)), ''.join(reversed(aligned_t))

def solve_edita(file_content):
    sequences = [str(record.seq) for record in SeqIO.parse(StringIO(file_content), "fasta")]
    s, t = sequences[0], sequences[1]
    edit_distance, aligned_s, aligned_t = edta(s, t)
    return edit_distance, aligned_s, aligned_t

with open("/Users/han3/Downloads/rosalind_edta.txt") as file:
    file_content = file.read()

edit_distance, aligned_s, aligned_t = solve_edita(file_content)
print(edit_distance)
print(aligned_s)
print(aligned_t)
