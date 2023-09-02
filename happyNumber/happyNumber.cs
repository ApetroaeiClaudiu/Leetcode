public class Solution {
    public bool IsHappy(int n) {
        Dictionary<int,int> occurences = new Dictionary<int, int>();
        int verif = n;
        int x;
        int aux;
        
        while ( n != 1 ) {
            aux = n;
            n = 0;
            while( aux != 0) {
                x = aux%10;
                n = n + x*x;
                aux = aux/10;
            }
            if (occurences.ContainsKey(n)) {
                return false;
            } else {
                occurences.Add(n, 1);
            }
        }
        if ( n == 1) {
            return true;
        }
        return false;
    }
}
