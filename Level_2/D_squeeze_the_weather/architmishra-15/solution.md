# 2D: architmishra-15

## My Enigma number

E = 122433

## 2D: Squeeze the weather report

### My days (with working) and my 16-day report:
Last 3 digits of E: `433`.
d1 = 4, d2 = 3, d3 = 3.

- Cloudy (C) = 1 + (4 % 4) = 1 + 0 = **1**
- Rain (R) = 1 + (3 % 3) = 1 + 0 = **1**
- Thunder (T) = 1 + (3 % 2) = 1 + 1 = **2**
- Sunny (S) = 16 - 1 - 1 - 2 = **12**

**My 16-day report:**
`S, S, S, S, S, S, S, S, S, S, S, S, T, T, R, C`

### My guess:
Because there is a massive bias toward Sunny days, I can map 'S' to just a single bit (like `0`). The fewer days (C, R, T) will take longer strings, but because they rarely happen, the total length will drop dramatically. My guess is around 22 bits.

### My code, my report encoded, and decoded back:
**My Code:** (Prefix code ensuring no codeword starts with another)
- S = `0` (1 bit)
- T = `10` (2 bits)
- R = `110` (3 bits)
- C = `111` (3 bits)

**My report encoded:**
`0000000000001010110111`

**Decoded back:**
Because no codeword is the prefix of another, we can read left to right:
Every `0` strictly isolates an S.
`10` isolates T. `110` isolates R. `111` isolates C.
Decoding yields exactly: 12 S's, 2 T's, 1 R, 1 C.

### My best code and its number of bits:
The Huffman-style prefix code I designed above is mathematically optimal for this distribution.
Number of bits used: (12 × 1) + (2 × 2) + (1 × 3) + (1 × 3) = **22 bits.**

### 16 × H (with working), and how close my best code is:
Formula: `16 × H = S × log₂(16 ÷ S) + C × log₂(16 ÷ C) + R × log₂(16 ÷ R) + T × log₂(16 ÷ T)`
Using the provided table for the logs:
- S (12 days): `12 × 0.415 = 4.98`
- T (2 days): `2 × 3 = 6`
- R (1 day): `1 × 4 = 4`
- C (1 day): `1 × 4 = 4`

**16 × H = 4.98 + 6 + 4 + 4 = 18.98 bits.**
My best code used 22 bits. I got very close to Shannon's absolute theoretical limit, missing it by only ~3 bits. (You can't have fractional bits in a simple discrete character code).

### Counting all reports vs shorter bit strings, and what it proves:
There are 4 kinds of weather over 16 days.
Total possible 16-day reports = $4^{16} = 2^{32} = 4,294,967,296$.

The number of different bit strings shorter than 32 bits (lengths 0 through 31) is the sum of powers of 2 up to 31:
$2^0 + 2^1 + 2^2 + ... + 2^{31} = 2^{32} - 1 = 4,294,967,295$.

**What this proves (Breaking Claim 3):**
By the Pigeonhole Principle, there is exactly 1 fewer short bit string ($2^{32} - 1$) than there are possible reports ($2^{32}$). Therefore, it is mathematically impossible to compress *every* possible report to fewer than 32 bits; at least one report must map to a string of 32 bits or longer. 

### Why common weather gets shorter codewords, and what H measures:
Common weather gets shorter codewords so that the occurrences you type the most take up the least space, which aggressively pulls down the average length of the entire message.
**H (Shannon's Entropy)** measures the intrinsic "surprise" or unpredictability of a data source. If you live in a desert, a "Sunny" report contains almost zero surprise (low entropy) and can be heavily compressed. A "Rain" report is highly surprising (high entropy) and carries a lot of information, requiring more bits to communicate.

## What surprised me
I was surprised that I could squash a 32-bit report down to 22 bits so easily just by swapping out equal-length codes for variable-length ones based on frequency. 

## Did I use AI? For what?
Yeaaahhh, for the starting part.
