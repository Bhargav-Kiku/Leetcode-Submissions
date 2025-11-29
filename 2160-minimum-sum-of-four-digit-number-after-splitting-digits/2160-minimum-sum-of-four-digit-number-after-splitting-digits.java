class Solution {
    public int minimumSum(int num) {
        List<Integer> s = new ArrayList<>();
        while (num > 0) {
            s.add(num % 10);
            num /= 10;
        }
        Collections.sort(s);
        return s.get(0) * 10 + s.get(1) * 10 + s.get(2) + s.get(3);
    }
}