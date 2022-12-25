
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        visit = {}
        def dfs(node:'Node') ->'Node':
            cur = Node(node.val)
            visit[cur.val] = cur
            curNeighbor = []
            for i in node.neighbors:
                if i.val not in visit.keys():
                    curNeighbor.append(dfs(i))
                else :
                    curNeighbor.append(visit[i.val])
            cur.neighbors = curNeighbor
            return cur
        if not node:
            return node
        else:
            return dfs(node)