class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}

        if (s == "" and t != "") or (t == "" and s != ""):
            return False

        elif s == "" and t == "":
            return True

        for char in s:
            count = s_dict.get(char, 0)
            s_dict[char] = count + 1

        for char in t:
            count = t_dict.get(char, 0)
            t_dict[char] = count + 1

        for key, value in s_dict.items():
            t_count = t_dict.get(key, 0)
            if value != t_count:
                return False
        
        for key, value in t_dict.items():
            s_count = s_dict.get(key, 0)
            if value != s_count:
                return False

        return True

        