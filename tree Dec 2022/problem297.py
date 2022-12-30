class Codec:
    
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        queue = []
        def serializehelper(root):
            nonlocal queue
            if not root:
                queue.append("N")
                return
            else:
                queue.append(str(root.val))
            serializehelper(root.left)
            serializehelper(root.right)
        serializehelper(root)
        queue = ",".join(queue)
        return queue
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(",")
        self.i = 0

        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()