<?php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function romanToInt($s) {
        $romans = [
            'M' => 1000,
            'D' => 500,
            'C' => 100,
            'L' => 50,
            'X' => 10,
            'V' => 5,
            'I' => 1,
        ];
        $result = $romans[$s[strlen($s)-1]];

        for ($i=strlen($s) - 2; $i>=0;$i--){
            if($romans[$s[$i]] >= $romans[$s[$i+1]]){
                $result = $result + $romans[$s[$i]];
            } else {
                $result = $result - $romans[$s[$i]];
            }
        }
        return $result;
    }
}
