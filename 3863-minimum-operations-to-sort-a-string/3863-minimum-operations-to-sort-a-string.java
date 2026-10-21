class Solution {
    public int minOperations(String s) {
        int n = s.length();
        boolean sorted = true;
        for (int i = 0; i < n - 1; i++) {
            if (s.charAt(i) > s.charAt(i + 1)) {
                sorted = false;
                break;
            }
        }
        if (sorted) return 0;
        if (n == 2) return -1;
        
        int minIdx = 0;
        int maxIdx = 0;
        
        for (int i = 0; i < n; i++) {
            if (s.charAt(i) < s.charAt(minIdx)) {
                minIdx = i;
            }
            if (s.charAt(i) >= s.charAt(maxIdx)) {
                maxIdx = i;
            }
        }
        if (minIdx == 0 || maxIdx == n - 1) {
            return 1;
        }
        if (minIdx == n - 1 && maxIdx == 0) {
            return 3;
        }
        return 2;
    }
}