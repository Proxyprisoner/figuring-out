"""the formula for trailing zeroes in factorial is n/5 + n/25 + n/125 + .... until n/5^k is 0
This is because every pair of 2 and 5 contributes to a trailing zero, and there are usually more factors of 2 than 5 in a factorial.
 Therefore, counting the number of factors of 5 gives us the number of trailing zeroes."""    

class Solution(object):
    def trailingZeroes(self, n):
        count=0
        while(n>0):
            n//=5
            count+=n
        return count
