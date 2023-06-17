/*
 * @lc app=leetcode.cn id=226 lang=typescript
 *
 * [226] 翻转二叉树
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

// Recursive
function invertTree(root: TreeNode | null): TreeNode | null {
  if (!root) return null;
  [root.left, root.right] = [invertTree(root.right), invertTree(root.left)]
  return root
};

// Interation
// function invertTree(root: TreeNode | null): TreeNode | null {
//   if (!root) return null;
//   const stack = [root]
//   while (stack.length) {
//     const node = stack.pop()
//     if (node) {
//       [node.left, node.right] = [node.right, node.left]
//       node.left && stack.push(node.left)
//       node.right && stack.push(node.right)
//     }
//   }
//   return root
// };

// @lc code=end
