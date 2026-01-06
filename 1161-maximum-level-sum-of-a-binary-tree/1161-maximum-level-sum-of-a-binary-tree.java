/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int maxLevelSum(TreeNode root) {
        Deque<TreeNode> q = new ArrayDeque<>();
        q.offerLast(root);
        int res = root.val;
        int l = 1;
        int cl = 0;
        while (!q.isEmpty()) {
            int s = 0;
            cl += 1;
            int toloop = q.size();
            for (int i = 0; i < toloop; i++) {
                TreeNode n = q.pollFirst();
                s += n.val;
                if (n.left != null) {
                    q.offerLast(n.left);
                }
                if (n.right != null) {
                    q.offerLast(n.right);
                }
            }
            if (s > res) {
                res = s;
                l = cl;
            }
            // System.out.println(s + " " + cl + " " + l);
        }
        return l;
    }
}