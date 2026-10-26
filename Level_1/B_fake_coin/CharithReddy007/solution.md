# 1B: CharithReddy007

## My Enigma number

GitHub username (lowercase): `charithreddy007`

E = 177079

| Character | Value | Multiplier | Product |
| --------- | ----- | ---------- | ------- |
| c | 3 | 1 | 3 |
| h | 8 | 2 | 16 |
| a | 1 | 4 | 4 |
| r | 18 | 8 | 144 |
| i | 9 | 16 | 144 |
| t | 20 | 32 | 640 |
| h | 8 | 64 | 512 |
| r | 18 | 128 | 2304 |
| e | 5 | 256 | 1280 |
| d | 4 | 512 | 2048 |
| d | 4 | 1024 | 4096 |
| y | 25 | 2048 | 51200 |
| 0 | 0 | 4096 | 0 |
| 0 | 0 | 8192 | 0 |
| 7 | 7 | 16384 | 114688 |

Total: E = 177079

---

## 1B: Find the fake coin

### My n

The rule is n = 10 + (E mod 90).

177079 = 90 × 1967 + 49

Therefore, n = 10 + 49 = **59 coins**.

### My guess for 27 coins

I guessed **5 weighings**. My thinking was to keep halving: 27 → 14 → 7 → 4 → 2 → 1.

### Halving on 27 coins (worst case)

Weigh 13 coins against 13 coins and leave one coin off the scale.

- If one pan is heavier, the fake is among the 13 coins on that pan.
- If the pans balance, the coin left aside is fake.

In the worst case, the candidate set shrinks as 27 → 13 → 6 → 3 → 1. This takes **4 weighings**.

### My table (2 to 27 coins)

The minimum number of weighings is the smallest k such that 3^k ≥ n, because each weighing has three possible outcomes.

| Coins | Minimum weighings | Coins | Minimum weighings |
|------:|------------------:|------:|------------------:|
| 2 | 1 | 15 | 3 |
| 3 | 1 | 16 | 3 |
| 4 | 2 | 17 | 3 |
| 5 | 2 | 18 | 3 |
| 6 | 2 | 19 | 3 |
| 7 | 2 | 20 | 3 |
| 8 | 2 | 21 | 3 |
| 9 | 2 | 22 | 3 |
| 10 | 3 | 23 | 3 |
| 11 | 3 | 24 | 3 |
| 12 | 3 | 25 | 3 |
| 13 | 3 | 26 | 3 |
| 14 | 3 | 27 | 3 |

### The rule

With k weighings, there are at most 3^k possible sequences of results. Therefore, k weighings can distinguish at most 3^k candidate coins. The minimum number is the smallest k for which 3^k is at least the number of coins.

The number of weighings increases at 4 coins (from 1 to 2) and at 10 coins (from 2 to 3) in the table from 2 to 27.

### My prediction and my weighing plan

For 59 coins, 3^3 = 27, which is too few, while 3^4 = 81. So my prediction is **4 weighings in the worst case**.

Label the coins 1–59. At each weighing, split the current candidates into three groups as evenly as possible. The two groups on the pans must be the same size; the group left off can differ from them by one coin. Keep the heavier group if the scale tips, or the group left off if the pans balance. The worst case is always the largest of the three groups.

One concrete sequence of group sizes is:

1. **59 candidates:** split into groups of 20, 20 and 19. Weigh 20 against 20. If unbalanced, keep the heavier 20; if balanced, keep the unweighed 19.
2. **At most 20 candidates:** split into groups of 7, 7 and 6 (for 20) or as evenly as possible for 19. Weigh the two equal groups. Keep the heavier group if unbalanced, otherwise keep the group left off the scale.
3. **At most 7 candidates:** split into groups of 2, 2 and 3. Weigh the two groups of 2. If one is heavier, keep that pair; if balanced, keep the unweighed group of 3.
4. **At most 3 candidates:** weigh one coin against another. If one is heavier, it is fake; if they balance, the third coin is fake.

At each stage, the heavier result identifies the group containing the fake, and a balance identifies the group that was not weighed. The worst case is four weighings.

### Why three groups beat two

A balance scale has three possible outcomes: left heavier, right heavier, or balanced. A well-designed weighing can therefore divide the candidates into three groups, reducing the search space by roughly a factor of three instead of two.

### Why no plan can do better

After k weighings there are at most 3^k possible result sequences, so there are at most 3^k different coins that can be uniquely identified. Since 3^3 = 27 < 59, three weighings cannot guarantee identifying one of 59 coins. Four weighings are sufficient because 3^4 = 81 ≥ 59.

## What surprised me

My guess of 5 was wrong twice over. Even halving only needs 4 for 27 coins, because leaving one coin off the scale already uses the "balanced" result a little. Splitting into three equal groups needs just 3 (27 → 9 → 3 → 1). The "balanced" result isn't wasted: it tells you as much as a tip does. Also, 59 coins needs only one more weighing than 27, and 4 weighings would still be enough for up to 81 coins.

## Did I use AI? For what?

Yes. I used AI tools (Claude and another assistant) to help draft this solution: the Enigma number and n calculation, the table, the 3^k rule, the 59-coin weighing plan and the explanations. I checked the table and traced the worst case of my plan (59 → 20 → 7 → 3 → 1) myself.
