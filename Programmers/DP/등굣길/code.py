def solution(m, n, puddles):
    # 행 : n
    # 열 : m
    count = [[0 for o in range(m+1)] for p in range(n+1)]
    count[1][1] = 1
    
    for i in range(1,n+1):
        for j in range(1,m+1):
            if [j,i] in puddles or [i, j] == [1, 1] :
                continue
            else:
                count[i][j] = count[i-1][j] + count[i][j-1]

    return count[-1][-1]% 1000000007
