class Solution:
    def myPow(self, x: float, n: int) -> float:
        def qpow(a: float, n: int) -> float:
            # TODO: implement
            pass
        return qpow(x, n) if n >= 0 else 1 / qpow(x, -n)
