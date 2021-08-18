class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def bfs(root):
    array = []
    if root:
        queue = [root]
        while queue:
            node = queue.pop(0)
            array.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return array


def dfs(root, array=None):
    if array is None:
        array = []
    if root:
        # array.append(root.val)  # PreOrder
        dfs(root.left, array)
        # array.append(root.val)  # InOrder
        dfs(root.right, array)
        array.append(root.val)  # PostOrder
    return array


def dfs_level(root, level, level_hash):
    # if level_hash is None:
    #     level_hash = {}
    if root:
        if level not in level_hash:
            level_hash[level] = [root.val]
        else:
            level_hash[level].append(root.val)
        dfs_level(root.left, level + 1, level_hash)
        dfs_level(root.right, level + 1, level_hash)
    return level_hash


head = TreeNode(1)
head.left = TreeNode(2)
head.right = TreeNode(3)
head.left.left = TreeNode(4)
head.left.right = TreeNode(5)
head.right.left = TreeNode(6)
head.right.right = TreeNode(7)

print('BFS', bfs(head))
print('DFS', dfs(head))
print('DFS_LEVEL', dfs_level(head, 0, {}))
