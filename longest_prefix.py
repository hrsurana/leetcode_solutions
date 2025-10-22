class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        lcp = ""
        i=0
        for w in strs[0]:
            for s in strs[1:]:
                if (len(s) < i+1 or s[i]!=w):
                        return lcp
            lcp = lcp + w
            i = i + 1
        return (lcp)
    