class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 0
        longest = 0
        substring = set()
        while j <= len(s) - 1:
            if s[j] in substring:
                longest = max(longest, len(substring))
                substring.remove(s[i])
                i += 1
            else:
                substring.add(s[j])
                longest = max(longest, len(substring))
                j+=1

        return longest
            