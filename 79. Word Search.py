Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        cols = len(board)
        rows = len(board[0])
        # x,y = 0,0
        
        for i in range(cols):
            for j in range(rows):
                if self.dfs(cols, rows,i, j, word, board, 0):
                    return True      
        return False
        
        
    def dfs(self, cols, rows, x, y, word, board, index):
        move = [(1,0),(0,1),(-1,0),(0,-1)]
        if index == len(word):
            return True
        if x < 0 or x >= cols or y < 0 or y >= rows:
            return False
        if board[x][y] != word[index]:
            return False
        
        curr = board[x][y]
        board[x][y] = ""
        for i, j in move:
            exist = self.dfs(cols,rows,x+i,y+j,word,board,index + 1)
            if exist:
                return True
                
        board[x][y] = curr
        return exist
