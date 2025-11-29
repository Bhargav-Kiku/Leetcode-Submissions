class Solution {
    public List<Integer> stableMountains(int[] height, int threshold) {
        List<Integer> res = new ArrayList<>();
        int n = height.length;
        for (int i = 1; i < n; i++){
            if (height[i-1] > threshold)
                res.add(i);
        }
        return res;
    }
}