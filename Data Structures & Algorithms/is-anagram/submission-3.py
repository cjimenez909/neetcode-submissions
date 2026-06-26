class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (s == "" and t != "") or (t == "" and s != ""):
            return False

        elif s == "" and t == "":
            return True

        s_dict = {}
        t_dict = {}

        for char in s:
            count = s_dict.get(char, 0)
            s_dict[char] = count + 1

        for char in t:
            count = t_dict.get(char, 0)
            t_dict[char] = count + 1

        return s_dict == t_dict

        