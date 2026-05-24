class Solution:
    def convertToTitle(self, col: int) -> str:
        res = ""

        while col > 0:
            col -= 1
            res = chr((col % 26) + ord("A")) + res
            col //= 26

        return res
        