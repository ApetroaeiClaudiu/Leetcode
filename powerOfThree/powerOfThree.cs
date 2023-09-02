public class Solution {
    public bool IsPowerOfThree(int n) {

      if ( n <= 0) {
          return false;
      } else {
          while (n > 1) {
              if (n%3 != 0) {
                  return false;
              }
              n = n/3;
          }
          if ( n == 1) {
              return true;
          } else {
              return false;
          }
      }
    }
}
