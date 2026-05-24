# Method - 1: Counter
# from collections import Counter

# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         return not (Counter(ransomNote) - Counter(magazine))

# Method 2: Hashmap
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_hash = {}

        for letter in magazine:
            mag_hash[letter] = 1 + mag_hash.get(letter, 0)
        
        for letter in ransomNote:
            if letter not in mag_hash or mag_hash[letter] <= 0:
                return False
            mag_hash[letter] -= 1

        return True