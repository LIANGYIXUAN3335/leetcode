# class Solution:
#     def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
#         res = []
#         for word in words:
#             stableboard = board
#             if self.exist(stableboard,word):
#                 res.append(word)
#         return res
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
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.refs = 0

    def addWord(self, word):
        cur = self
        cur.refs += 1
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            cur.refs += 1
        cur.isWord = True

    def removeWord(self, word):
        cur = self
        cur.refs -= 1
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
                cur.refs -= 1


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)

        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r, c, node, word):
            if (
                r not in range(ROWS) 
                or c not in range(COLS)
                or board[r][c] not in node.children
                or node.children[board[r][c]].refs < 1
                or (r, c) in visit
            ):
                return

            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                node.isWord = False
                res.add(word)
                root.removeWord(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visit.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)