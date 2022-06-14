class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        a = collections.Counter(s1)
        b = collections.Counter(s2)
        if a!=b:
            return False
        r = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                r += 1
        return r < 3 
