# 2A: architmishra-15

## My Enigma number
E = 122433

My guess: **Collision would indeed occur**

## Working -
We can prove that a collision would occur in the original system by the Pigeonhole Principle.

**Max length of GitHub username:** 39
**Total number of allowed characters:** 26 (letters) + 10 (digits) + 1 (hyphen) = 37
Therefore, Total number of possible GitHub usernames = 37^39

**Highest Possible Enigma Number:** E_max = 26 * (2^39 - 1) ≈ 1.43 × 10^13

**Conclusion by the Pigeonhole Principle:**
Because the number of possible usernames (37^39) is astronomically larger than the number of possible Enigma numbers (≈ 1.43 × 10^13), multiple usernames are mathematically guaranteed to map to the same Enigma number.

### Twin 1 (Simple Twin):
A simple twin is found by swapping a character for another that has the exact same base value. Both `-` and `0` have a value of 0.
Original: `architmishra-15`
Twin 1: `architmishra015`
(The E value remains exactly 122433 because the mathematical sum does not change).

### Twin 2 (Smarter Twin 1):
Let's take the first two letters: `a` (1) & `r` (18). 
(1 × 1) + (18 × 2) = 37.
Replace them with `c` (3) and `q` (17):
(3 × 1) + (17 × 2) = 37.
Therefore, **The first smarter twin name:** ***cqchitmishra-15***

### Twin 3 (Smarter Twin 2):
Let's take the third and fourth letters: `c` (3) and `h` (8).
Original Sum: (3 × 4) + (8 × 8) = 76.
Replace them with `e` (5) and `g` (7):
New Sum: (5 × 4) + (7 × 8) = 76.
Therefore, **The second smarter twin name:** ***aregitmishra-15***

### The two reasons for collisions:
1. **Duplicate character values:** Certain characters in the original rule share the exact same assigned value (e.g., `-` and `0` are both worth 0; `a` and `1` are both worth 1). Swapping these guarantees an identical E.
2. **Algebraic sum overlap:** The multiplier (2^n) is too small compared to the max character value (26), allowing combinations of smaller/larger characters to yield the exact same sum.

## My new rule
To avoid collision, we need to ensure every single character sequence maps to a completely unique hash. 
1. First, assign every allowed character (letters, numbers, hyphen) a strictly unique value from 1 to 37 (e.g., `a-z` = 1-26, `0-9` = 27-36, `-` = 37) so no two characters share a value.
2. Instead of multiplying by 2^n, multiply by 37^n (where n is the character's position index).

## Why it can never collide
By assigning each character a unique value from 1 to 37 and multiplying by 37^n, we are essentially converting the username into a **Base-37 positional numeral system**. Just like the decimal (base-10) system uses powers of 10 to ensure every sequence of digits forms a unique number, using powers of 37 ensures every combination of characters forms a strictly unique Enigma number. Because this forms a bijective mapping, you can perfectly reverse the mathematical process (using modulo 37 arithmetic) to decode the exact username from the number. Therefore, no two usernames can ever map to the same number.

## What surprised me
I was able to apply Pigeonhole Principle in the first go for the initial collision proof, lol.

## Did I use AI? For what?
Nope, I did not use AI for this task :)
