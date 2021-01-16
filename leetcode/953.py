class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_index = {c: i for i, c in enumerate(order)}
        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            m = min(len(word1), len(word2))
            for j in range(m):
                char1 = word1[j]
                char2 = word2[j]
                if char1 != char2:
                    if order_index[char1] > order_index[char2]:
                        return False
                    break
            if word1[:m] == word2[:m] and len(word1) > len(word2):
                return False

        return True
