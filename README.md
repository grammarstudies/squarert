# squarert
A hobby project for analyzing the efficacy of a shortcut for calculating square roots

Said shortcut goes as follows:
Take the number for which you will calculate the square root (e.g. 32).
Then, find its nearest perfect square (in the case of 32, 36).
Record the square root of that perfect square (6).
Add to that number a fraction, the numerator of which will be the difference between the imperfect square and the perfect square (32 - 36 = -4). The denominator will be the double of the perfect square root (12). You are then left with 6 -4/12, or 6 -1/3, or ~5.67.

This program takes the difference between the square root calculated via the above shortcut (~5.67) and the actual calculated square root (~5.66) for any given non-negative number.
