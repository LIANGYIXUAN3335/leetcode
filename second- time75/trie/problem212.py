class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        head = TrieNode()
        res = set()
        m = len(board)
        n = len(board[0])
        def backtracking(i,j,curnode):
            if board[i][j] not in curnode.children:
                return
            temp = curnode
            curnode = curnode.children[board[i][j]]
            if curnode.word:
                res.add(curnode.word)
                curnode.word = None
            char = board[i][j]
            board[i][j] = None
            for i1, j1 in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= i1 < m and 0 <= j1 < n:
                    backtracking(i1, j1, curnode)
            board[i][j] = char
            if not curnode.children:
                temp.children.pop(char)
        if not board:
            return res
        for i in words:
            head.addword(i)
        for i in range(m):
            for j in range(n):
                backtracking(i,j,head)
        return list(res)
                        
    
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None
    def addword(self,word):
        cur = self
        for i in word:
            if i not in cur.children:
                cur.children[i] = TrieNode()
            cur = cur.children[i]
        cur.word = word

# from collections import defaultdict


# class Trie:
#     def __init__(self):
#         self.children = defaultdict(Trie)
#         self.word = ""

#     def insert(self, word):
#         cur = self
#         for c in word:
#             cur = cur.children[c]
#         cur.is_word = True
#         cur.word = word


# class Solution:
#     def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
#         trie = Trie()
#         for word in words:
#             trie.insert(word)
		
#         def dfs(now, i1, j1):
#             if board[i1][j1] not in now.children:
#                 return

#             ch = board[i1][j1]

#             nxt = now.children[ch]
#             if nxt.word != "":
#                 ans.append(nxt.word)
#                 nxt.word = ""

#             if nxt.children:
#                 board[i1][j1] = "#"
#                 for i2, j2 in [(i1 + 1, j1), (i1 - 1, j1), (i1, j1 + 1), (i1, j1 - 1)]:
#                     if 0 <= i2 < m and 0 <= j2 < n:
#                         dfs(nxt, i2, j2)
#                 board[i1][j1] = ch

#             if not nxt.children:
#                 now.children.pop(ch)

#         ans = []
#         m, n = len(board), len(board[0])

#         for i in range(m):
#             for j in range(n):
#                 dfs(trie, i, j)

#         return ans

# class TrieNode:
#     def __init__(self):
#         self.children = {}
#         self.isWord = False
#         self.refs = 0

#     def addWord(self, word):
#         cur = self
#         cur.refs += 1
#         for c in word:
#             if c not in cur.children:
#                 cur.children[c] = TrieNode()
#             cur = cur.children[c]
#             cur.refs += 1
#         cur.isWord = True

#     def removeWord(self, word):
#         cur = self
#         cur.refs -= 1
#         for c in word:
#             if c in cur.children:
#                 cur = cur.children[c]
#                 cur.refs -= 1


# class Solution:
#     def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
#         root = TrieNode()
#         for w in words:
#             root.addWord(w)

#         ROWS, COLS = len(board), len(board[0])
#         res, visit = set(), set()

#         def dfs(r, c, node, word):
#             if (
#                 r not in range(ROWS) 
#                 or c not in range(COLS)
#                 or board[r][c] not in node.children
#                 or node.children[board[r][c]].refs < 1
#                 or (r, c) in visit
#             ):
#                 return

#             visit.add((r, c))
#             node = node.children[board[r][c]]
#             word += board[r][c]
#             if node.isWord:
#                 node.isWord = False
#                 res.add(word)
#                 root.removeWord(word)

#             dfs(r + 1, c, node, word)
#             dfs(r - 1, c, node, word)
#             dfs(r, c + 1, node, word)
#             dfs(r, c - 1, node, word)
#             visit.remove((r, c))

#         for r in range(ROWS):
#             for c in range(COLS):
#                 dfs(r, c, root, "")

#         return list(res)
