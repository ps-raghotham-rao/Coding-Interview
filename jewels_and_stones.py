class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        c=0
        # print(jewels1)
        for i in stones:
            if i in jewels:
                c+=1
        return c

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        c=0
        # print(jewels1)
        seti = set(jewels)
        for i in stones:
            if i in seti:
                c+=1
        return c