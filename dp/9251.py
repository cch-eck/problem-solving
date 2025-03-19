# LCS: longest common subsequence
'''
점화식을 찾아야 함.
def LCS(a,b):
    return

LCS(ACAYKP, CAPCAK)
= LCS(ACAYK, CAPCAK)
= LCS(ACAY, CAPCA)+1 = LCS(ACA, CAPCA)+1
= LCS(A, CAP)+3
= LCS(A,A)+3 = 4
A CA           A C           CA
if first[i] == second[j]
dp[1][2] = max(dp[1][1], dp[0][2])+1

ACA APCAK
if first[i] = second[j]
dp[1][1] = 1
dp[2][1] = max(dp[1][1], dp[2][0])= 1
dp[2][2] = max(dp[2][1], dp[1][2])

ACA C            A C         AC 
dp[3][1] = max(dp[1][1], dp[3][0])
ACA CA
dp[3][2] = max(dp[3][1], dp[2][2])+1

D[i][j] = LCS(앞 단어 i번째 글자, 뒷 단어 j번째 글자까지)
'''
first = input()
second = input()
first_len, second_len = len(first), len(second)
D = [[0 for _ in range(second_len+1)] for _ in range(first_len+1)]

for i in range(first_len):
    for j in range(second_len):
        if first[i] == second[j]:
            D[i][j] = D[i-1][j-1]+1
        else:
            D[i][j] = max(D[i][j-1], D[i-1][j])

print(D[first_len-1][second_len-1])

# for i in range(first_len):
#     for j in range(second_len):
#         print(f"LCS[{i}][{j}]= {D[i][j]}")