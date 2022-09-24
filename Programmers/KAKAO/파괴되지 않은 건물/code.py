def solution(board, skills):
    
    test_board = [ [0 for _ in range(len(board[0])+1)] for _ in range(len(board)+1)] 
    
    for s_type, r1, c1, r2, c2, degree in skills:
        test_board[r1][c1] += degree if s_type == 2 else -degree
        test_board[r1][c2+1] += -degree if s_type == 2 else degree 
        test_board[r2+1][c1] += -degree if s_type == 2 else degree
        test_board[r2+1][c2+1] += degree if s_type == 2 else -degree
    
    # 가로 더하기
    for j in range(1, len(test_board[0])):
        for i in range(len(test_board)):
            test_board[i][j] += test_board[i][j-1] 
                       
    # 세로 더하기
    for i in range(1, len(test_board)):
        for j in range(len(test_board[0])):
            test_board[i][j] += test_board[i-1][j] 
    
    answer = 0
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            answer += 1 if board[i][j] + test_board[i][j] > 0 else 0
            board[i][j] += test_board[i][j]
    
    
    return answer
