class Codec:
    
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        queue = []
        def serializehelper(root):
            if root == None:
                queue.append("N")
                return
            queue.append(root.val)
            serializehelper(root.left)
            serializehelper(root.right) 
        serializehelper(root)
        return ','.join(str(i) for i in queue)
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(",")
        if data[0] == "N":
            return None
        index = 0
        def deserializehelper():
            nonlocal index
            if data[index] == "N":
                index += 1
                return None
            cur = TreeNode(data[index])
            index += 1
            cur.left = deserializehelper()
            cur.right = deserializehelper()
            return cur
        head = deserializehelper()
        return head
        