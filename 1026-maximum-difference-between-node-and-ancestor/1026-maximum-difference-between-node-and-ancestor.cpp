/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
private:
    int max_diff = 0;
    void dfs(TreeNode* root, int maxv, int minv) {
        if (root == nullptr) {
            max_diff = max(max_diff, maxv - minv);
            return;
        }
        maxv = max(maxv, root->val);
        minv = min(minv, root->val);
        dfs(root->left,maxv,minv);
        dfs(root->right,maxv,minv);
    }
public:
    int maxAncestorDiff(TreeNode* root) {
        if (root == nullptr) {
            return 0;
        }
        dfs(root, root->val, root->val);
        return max_diff;
    }
};