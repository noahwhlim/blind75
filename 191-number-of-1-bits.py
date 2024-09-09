class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        num = bin(n)[2:]
        for c in num:
            if c == '1':
                count += 1
        return count