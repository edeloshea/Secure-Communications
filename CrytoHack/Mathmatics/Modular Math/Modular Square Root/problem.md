In Legendre Symbol we introduced a fast way to determine whether a number is a square root modulo a prime. We can go further: there are algorithms for efficiently calculating such roots. The best one in practice is called Tonelli-Shanks, which gets its funny name from the fact that it was first described by an Italian in the 19th century and rediscovered independently by Daniel Shanks in the 1970s.

All primes that aren't 2 are of the form p ≡ 1 mod 4 or p ≡ 3 mod 4, since all odd numbers obey these congruences. As the previous challenge hinted, in the p ≡ 3 mod 4 case, a really simple formula for computing square roots can be derived directly from Fermat's little theorem. That leaves us still with the p ≡ 1 mod 4 case, so a more general algorithm is required.

In a congruence of the form r2 ≡ a mod p, Tonelli-Shanks calculates r.

Tonelli-Shanks doesn't work for composite (non-prime) moduli. Finding square roots modulo composites is computationally equivalent to integer factorization.

The main use-case for this algorithm is finding elliptic curve co-ordinates. Its operation is somewhat complex so we're not going to discuss the details, however, implementations are easy to find and Sage has one built-in.

Find the square root of a modulo the 2048-bit prime p. Give the smaller of the two roots as your answer.

output.txt