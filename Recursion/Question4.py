class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def constructBinaryTree(s):
    def build_tree(start, end):
        if start > end:
            return None

        i = start
        while i <= end and s[i] not in ('(', ')'):
            i += 1

        root_val = int(s[start:i])
        root = TreeNode(root_val)

        j = i
        balance = 0
        while j <= end:
            if s[j] == '(':
                balance += 1
            elif s[j] == ')':
                balance -= 1

            if balance == 0:
                break
            j += 1

        root.left = build_tree(i + 1, j - 1)
        root.right = build_tree(j + 2, end - 1)

        return root

    return inorder_traversal(build_tree(0, len(s) - 1))


def inorder_traversal(root):
    if not root:
        return []

    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)


s = "4(2(3)(1))(6(5))"
result = constructBinaryTree(s)
print(result)
