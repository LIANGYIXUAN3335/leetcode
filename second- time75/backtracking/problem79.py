class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return True
        for i in range(len(board)):
            for j in range(len(board[0])):
                print(1)
                if self.backtracking(board,i,j,word,0):
                    return True
        return False
    def backtracking(self,board,i,j,word,index):
        if index  == len(word):
            return True
        if i  >= len(board) or j  >= len(board[0]) or i <0 or j < 0:
            return False 
        if board[i][j] == word[index]: 
            board[i ][j ] = ""
            res = self.backtracking(board,i+1,j,word,index + 1) or self.backtracking(board,i,j+1,word,index + 1) or self.backtracking(board,i-1,j,word,index + 1) or self.backtracking(board,i,j-1,word,index + 1)
            board[i ][j]  = word[index]
            return res
# class Solution:
#     def exist(self, board: List[List[str]], word: str) -> bool:
#         if not str:
#             return True
#         for i in range(len(board)):
#             for j in range(len(board[0])):
#                 if self.backtracking(board,i,j,word,0):
#                     return True
#         return False
#     def backtracking(self,board,i,j,word,index):
#         if index == len(word):
#             return True
#         if i  >= len(board) or j  >= len(board[0]) or i <0 or j < 0:
#             return False  
#         if board[i][j] == word[index]: 
#             board[i ][j ] = ""
#             res = self.backtracking(board,i+1,j,word,index + 1) or self.backtracking(board,i,j+1,word,index + 1) or self.backtracking(board,i-1,j,word,index + 1) or self.backtracking(board,i,j-1,word,index + 1)
#             board[i ][j]  = word[index]
#             return res