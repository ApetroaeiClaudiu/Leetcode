<?php
class Solution {

    /**
     * @param Integer $dividend
     * @param Integer $divisor
     * @return Integer
     */
    function divide($dividend, $divisor) {
        
        $sign = (($dividend < 0) ^
                ($divisor < 0)) ? -1 : 1;
        
        // remove sign of operands
        $dividend = abs($dividend);
        $divisor = abs($divisor);
        
        // Initialize
        // the quotient
        $quotient = 0;
        $temp = 0;
        
        // test down from the highest
        // bit and accumulate the
        // tentative value for valid bit
        for ($i = 31; $i >= 0; --$i)
        {
        
            if ($temp + ($divisor << $i) <= $dividend)
            {
                $temp += $divisor << $i;
                $quotient |= (double)(1) << $i;
            }
        }
        //if the sign value computed earlier is -1 then negate the value of quotient
        if($sign==-1)
        $quotient=-$quotient;
        if ($quotient > 2147483647) {
            return 2147483647;
        }
        return $quotient;
    }
}
