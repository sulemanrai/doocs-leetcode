class Solution:
    def countValidWords(self, sentence: str) -> int:
        def check(s: str) -> bool:
            # TODO: implement
            pass
        return sum(check(s) for s in sentence.split())
