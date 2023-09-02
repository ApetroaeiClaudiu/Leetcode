public class Solution {
    public int MySqrt(int x) {
        if ( x == 0 || x == 1) {
            return x;
        } else if ( x == 2 ) {
            return 1;
        }
        double root = x / 3;
        int i;
        for (i = 0; i < 32; i++)
            root = (root + x / root) / 2;
        return (int)root;
    }
}
