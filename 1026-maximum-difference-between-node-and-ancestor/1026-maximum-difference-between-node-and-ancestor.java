class Solution {
    public int maxAncestorDiff(TreeNode root) {
        if (root == null) {
            return 0;
        }
        return dfs(root, root.val, root.val);
    }

    private int dfs(TreeNode node, int minV, int maxV) {
        if (node == null) {
            return 0;
        }

        int currentMaxDiff = Math.max(Math.abs(node.val - minV), Math.abs(node.val - maxV));

        int newMinV = Math.min(minV, node.val);
        int newMaxV = Math.max(maxV, node.val);

        int leftDiff = dfs(node.left, newMinV, newMaxV);
        int rightDiff = dfs(node.right, newMinV, newMaxV);

        return Math.max(currentMaxDiff, Math.max(leftDiff, rightDiff));
    }
}