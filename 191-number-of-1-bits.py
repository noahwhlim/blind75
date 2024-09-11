class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        num = bin(n)[2:]
        for c in num:
            if c == '1':
                count += 1
        return count
        
# neetcode solution #1
# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         res = 0
#         while n:
#             res += n % 2
#             n = n >> 1
#         return res

# neetcode solution #2
# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         res = 0
#         while n:
#             n &= n - 1    # basically gets rid of next 1
#             res += 1
#         return res
