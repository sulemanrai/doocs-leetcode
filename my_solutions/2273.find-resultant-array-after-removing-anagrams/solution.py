class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        def check(s: str, t: str) -> bool:
            # TODO: implement
            pass
        return [words[0]] + [t for s, t in pairwise(words) if check(s, t)]
