# 2C: architmishra-15

## My Enigma number

E = 122433 

## 2C: The greedy cashier

### My tokens (with working):
Taking the last 3 digits of E: `433`.
- d1 = 4
- d2 = 3
- d3 = 3

Calculating tokens:
- a = 2 + d3 = 2 + 3 = **5**
- b = a + 1 + d2 = 5 + 1 + 3 = **9**
- c = b + 1 + d1 = 9 + 1 + 4 = **14**

**My tokens are:** {1, 5, 9, 14}

### My guess:
No, biggest-first (the greedy algorithm) will likely fail. Greedy algorithms usually only yield the mathematical minimum for specific, highly structured token sets (like standard denominations where each coin is at least twice the previous). Custom sets almost always break it.

### My table (amount, biggest-first, best):
I need to check up to $b + c - 1 = 9 + 14 - 1 = 22$.

| Amount | Biggest-First (Tokens) | Best (Tokens) |
| :--- | :--- | :--- |
| 1 | 1 | 1 |
| 2 | 2 | 2 |
| 3 | 3 | 3 |
| 4 | 4 | 4 |
| 5 | 1 | 1 |
| 6 | 2 | 2 |
| 7 | 3 | 3 |
| 8 | 4 | 4 |
| 9 | 1 | 1 |
| 10 | 2 (9,1) | 2 (5,5) |
| 11 | 3 (9,1,1) | 3 (9,1,1) |
| 12 | 4 (9,1,1,1) | 4 (9,1,1,1) |
| 13 | 5 (9,1,1,1,1) | 5 (9,1,1,1,1) |
| 14 | 1 | 1 |
| 15 | 2 | 2 |
| 16 | 3 | 3 |
| 17 | 4 | 4 |
| **18** | **5** | **2** |
| 19 | 6 | 3 |
| 20 | 3 | 3 |
| 21 | 4 | 4 |
| 22 | 5 | 4 |

### Smallest failing amount and both payments:
The smallest failing amount is **18**.
- **Biggest-first payment:** 14 + 1 + 1 + 1 + 1 (5 tokens)
- **Best payment:** 9 + 9 (2 tokens)

### Why biggest-first fails here:
Greedy blindly grabs the biggest possible token (14) because it fits inside 18. However, this leaves a remainder of 4. Because 4 is smaller than the next available tokens (9 and 5), the cashier is forced to fill the remaining gap entirely with 1s. By bypassing the 14, we leave exactly 18, which is perfectly divisible by the 9 token, requiring only two tokens total.

### Why the table method works:
The table method uses Dynamic Programming. The formula `1 + the smallest of best[x − t]` works because to arrive at amount `x`, you *must* hand over some final token `t`. If you already know the absolute fewest tokens needed to make the remaining amount (`x - t`), you just add 1 (for token `t`) to find the total. By checking this against *every* possible token `t` that fits, you are guaranteed to find the true minimum path to `x` without getting trapped in a "greedy" dead end.

## What surprised me
I was surprised that the greedy algorithm held on for so long (matching the best algorithm perfectly up to 17) before failing so dramatically at 18 (a difference of 3 tokens).

## Did I use AI? For what?
Nope.
