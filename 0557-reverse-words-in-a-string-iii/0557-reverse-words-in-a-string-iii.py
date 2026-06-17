class Solution:
    def reverseWords(self, s: str) -> str:

        words = s.split()

        for i in range(len(words)):

            word = list(words[i])

            left = 0
            right = len(word) - 1

            while left < right:

                word[left], word[right] = word[right], word[left]

                left += 1
                right -= 1

            words[i] = "".join(word)

        return " ".join(words)