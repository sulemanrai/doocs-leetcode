class Solution {
    static List<Integer> primes = new ArrayList<>();
    static {
        int x = 2;
        int M = 1000;
        while (primes.size() < M) {
            boolean is_prime = true;
            for (int p : primes) {
                if (p * p > x) {
                    break;
                }
                if (x % p == 0) {
                    is_prime = false;
                    break;
                }
            }
            if (is_prime) {
                primes.add(x);
            }
            x++;
        }
    }

    public int minNumberOfPrimes(int n, int m) {
        // TODO: implement
    }
}
