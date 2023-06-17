/*
 * @lc app=leetcode.cn id=226 lang=c
 *
 * [226] 翻转二叉树
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

// Iterative
struct TreeNode* invertTree(struct TreeNode* root){
    if (root == NULL) {
      return NULL;
    }
    struct TreeNode* stack[1000];
    int top = 0;
    stack[top++] = root;
    while (top > 0) {
      struct TreeNode* node = stack[--top];
      struct TreeNode* tmp = node->left;
      node->left = node->right;
      node->right = tmp;
      if (node->left != NULL) {
        stack[top++] = node->left;
      }
      if (node->right != NULL) {
        stack[top++] = node->right;
      }
    }
    return root;
}
// Recursive
// struct TreeNode* invertTree(struct TreeNode* root){
//   if (root == NULL) {
//     return NULL;
//   }
//   struct TreeNode* tmp = root->left;
//   root->left = root->right;
//   root->right = tmp;
//   invertTree(root->left);
//   invertTree(root->right);
//   return root;
// }
// https://medium.com/@mefengl/comparing-recursive-and-iterative-approaches-to-invert-a-binary-tree-9809dc800e66
// @lc code=end
