def longest_increasing_subsequence(sequence):
    n = len(sequence)
    dp = [1] * n
    parent = [-1] * n
    
    for i in range(n):
        for j in range(i):
            if sequence[j] < sequence[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                parent[i] = j

    max_index = dp.index(max(dp))
    lis = []
    while max_index != -1:
        lis.append(sequence[max_index])
        max_index = parent[max_index]
    return lis[::-1]

def longest_decreasing_subsequence(sequence):
    neg_sequence = [-x for x in sequence]
    return [-x for x in longest_increasing_subsequence(neg_sequence)]

def solve_lgis(permutation):
    lis = longest_increasing_subsequence(permutation)
    lds = longest_decreasing_subsequence(permutation)
    return lis, lds


with open("/Users/han3/Downloads/rosalind_lgis-4.txt") as file:
    lines = file.readlines()
    n = int(lines[0].strip())
    permutation = list(map(int, lines[1].strip().split()))

lis, lds = solve_lgis(permutation)

print(" ".join(map(str, lis)))
print(" ".join(map(str, lds)))
