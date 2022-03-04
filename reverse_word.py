# https://leetcode.com/problems/reverse-words-in-a-string-iii/ --Question

class Solution:
    def reverseWords(self, s: str) -> str:
        words=s.split()
        reverse_word=[word[::-1] for word in words]
        reverse_sentence=" ".join(reverse_word)
        return reverse_sentence