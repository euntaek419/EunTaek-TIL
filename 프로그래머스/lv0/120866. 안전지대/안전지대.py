def solution(board):
    
    count = 0
    
    long_board = [[0]*(len(board)+2) for i in range(len(board)+2)] #+2씩 확장된 보드
    
    for i in range(0, len(board)):
        for j in range(0, len(board)):
            if(board[i][j] == 1): #보드의 [i][j] == 1이면,
                long_board[i][j] = 1 #롱보드의 [i][j] == 1로 변경
    
    for ii in range(0, len(long_board)):
        for jj in range(0, len(long_board)):
            if(long_board[ii][jj] == 1 ): #보드의 [i][j] == 1이면,
                
                #주변의 숫자를 2로 변경
                if(long_board[ii+1][jj+1] == 0):
                    long_board[ii+1][jj+1] = 2
                    
                if(long_board[ii+1][jj-1] == 0):
                    long_board[ii+1][jj-1] = 2
                    
                if(long_board[ii-1][jj-1] == 0):
                    long_board[ii-1][jj-1] = 2
                    
                if(long_board[ii-1][jj+1] == 0):    
                    long_board[ii-1][jj+1] = 2
                
                if(long_board[ii][jj+1] == 0):
                    long_board[ii][jj+1] = 2
                    
                if(long_board[ii][jj-1] == 0):
                    long_board[ii][jj-1] = 2
                    
                if(long_board[ii+1][jj] == 0):
                    long_board[ii+1][jj] = 2
                    
                if(long_board[ii-1][jj] == 0):
                    long_board[ii-1][jj] = 2
                
                
    
    for iii in range(0, len(board)):
        for jjj in range(0, len(board)):
            if(long_board[iii][jjj] == 0):
                board[iii][jjj] = 0
            else:
                board[iii][jjj] = 1
    
    
    #1차원 배열로 변경
    board = sum(board, [])
    
    #반복문 사용해서 0의 갯수 카운트
    for k in range(0, len(board)):
        if(board[k] == 0):
            count = count + 1
    
    
    return count