class Solution {
    public int getSum(int a, int b) {
        while(a != 0){
            int carries = (a & b) << 1;
            b = a ^ b;
            a = carries;
            }
        return b;
    }
}