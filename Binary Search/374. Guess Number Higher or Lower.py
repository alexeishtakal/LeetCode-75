# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def bs(self, l, r):
        if r>=l:
            num = (l+r)//2
            g = guess(num)
            if g==0:
                return num
            elif g==-1:
                return self.bs(l, num-1)
            else:
                return self.bs(num+1, r)
        return None

    def guessNumber(self, n: int) -> int:
        return self.bs(1, n)

