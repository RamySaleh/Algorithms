from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        nm_str = ""
        for n in digits:
            nm_str = nm_str + str(n)

        new_number = str(int(nm_str) + 1)

        res = []
        for c in new_number:
            res.append(int(c))

        return res


r = Solution().plusOne([9])
print(r)