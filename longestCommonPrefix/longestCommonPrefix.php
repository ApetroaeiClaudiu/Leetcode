<?php
class Solution {

    /**
     * @param String[] $strs
     * @return String
     */
    function longestCommonPrefix($strs) {

        sort($strs);
        
        $firstString = $strs[0];
        $lastString = $strs[count($strs)-1];
        $len = min(strlen($firstString), strlen($lastString));

        for ($i=0; $i<$len && $firstString[$i]==$lastString[$i]; $i++); 

        return substr($firstString, 0, $i);
    }
}
