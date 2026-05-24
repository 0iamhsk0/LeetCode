class Solution:
    def reverseWords(self, s: str) -> str:
        stripped_string = s.split()
        ans = []

        for i in range(len(stripped_string) - 1, -1, -1):
            ans.append(stripped_string[i])
            if i != 0:
                ans.append(" ")

        return "".join(ans) 