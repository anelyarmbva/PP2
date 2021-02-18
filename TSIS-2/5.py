class Solution(object):
    def largestAltitude(self, gain):
        maxi, m = 0, 0
        for i in gain:
            m += i
            if m > maxi:
                maxi = m
        return maxi
        