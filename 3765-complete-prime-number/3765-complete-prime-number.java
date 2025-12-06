class Solution {
    private HashMap<Integer, Boolean> p = new HashMap<>();
    private Boolean isPrime(int x) {
        if (p.containsKey(x)) return p.get(x);
        if (x == 0) return true;
        if (x == 1) return false;
        for (int i = 2; i <= Math.sqrt(x); i++) {
            if (x % i == 0) {
                p.put(x,false);
                return false;
            }
        }
        p.put(x,true);
        return true;
    }
    public boolean completePrime(int num) {
        if (!isPrime(num)) return false;
        int tn = 10;
        while (tn < num) {
            int x = num % tn;
            tn *= 10;
            if (!isPrime(x)) return false;
        }
        while (tn/10 > 0) {
            int x = num / tn;
            tn /= 10;
            if (!isPrime(x)) return false;
        }
        return true;
    }
}