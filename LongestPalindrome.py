def longest_palindromic_substring(A):
    n = len(A)
    if n == 0:
        return ""

    dp = [[False for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dp[i][i] = True

    start = 0  
    max_length = 1  

    for i in range(n - 1):
        if A[i] == A[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_length = 2

    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if A[i] == A[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                if length > max_length:
                    start = i
                    max_length = length

    return A[start:start + max_length]


A = input()
print(longest_palindromic_substring(A)) 
