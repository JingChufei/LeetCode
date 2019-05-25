# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    # 递归思想 对于每一棵子二叉树 都有其相应的 前序遍历preorder 和 中序遍历inorder
    # buildTree函数 返回 根据preorder和inorder构造的二叉树的根节点
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        if preorder == []:
            return
        
        node = TreeNode(preorder[0])
        
        if len(preorder) == 1:
            return node
        
        # node 在中序遍历中的索引
        index_in = self.search(inorder, preorder[0])
        
        node.left = self.buildTree(preorder[1:index_in+1], inorder[:index_in])
        node.right = self.buildTree(preorder[index_in+1:], inorder[index_in+1:])
        
        return node
        
    
    # 寻找target在列表a中的索引
    def search(self, a, target):
        
        n = len(a)
        for i in range(n):
            if a[i] == target:
                return i
