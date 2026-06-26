class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict = {}
        t_dict = {}

        for char in s:
            count = s_dict.get(char, 0)
            s_dict[char] = count + 1

        for char in t:
            count = t_dict.get(char, 0)
            t_dict[char] = count + 1

        return s_dict == t_dict

        