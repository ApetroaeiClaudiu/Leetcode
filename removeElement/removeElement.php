<?php
class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $val
     * @return Integer
     */
    function removeElement(&$nums, $val) {
        $index = 0;
        for ( $i = 0; $i< count($nums); $i++){
            if($nums[$i] != $val){
                $nums[$index] = $nums[$i];
                $index++;
            }
        }

        return $index;
    }
}
