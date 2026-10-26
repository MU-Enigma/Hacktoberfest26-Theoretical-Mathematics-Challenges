# 1A: CharithReddy007

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

## 1A: The bridges of your city

**My last four digits:** 7079

### My map

The four outer bridges are P–Q, Q–R, R–S, and S–P. Each outer island also connects to C. Since the digits for P, R, and S are odd, each of those centre bridges has a second parallel bridge. Q's centre bridge remains single.

- P–Q: 1 bridge
- Q–R: 1 bridge
- R–S: 1 bridge
- S–P: 1 bridge
- P–C: 2 bridges
- Q–C: 1 bridge
- R–C: 2 bridges
- S–C: 2 bridges

**Total bridges: 11**

### My guess

I guessed it would be **impossible**. Königsberg was impossible, and my map has even more bridges (11), so I thought it would only be harder.

### My attempts

I numbered the double bridges as P–C₁/P–C₂, R–C₁/R–C₂, S–C₁/S–C₂.

**Attempt 1 (start at P):** P → Q → R → S → P → C (P–C₁) → P (P–C₂).
Stuck at P after 6 bridges: all 4 of P's bridges are used, but Q–C, R–C₁, R–C₂, S–C₁, S–C₂ are still left.

**Attempt 2 (start at C):** C → Q → P → S → R → Q.
Stuck at Q after 5 bridges: Q only has 3 bridges and all are used, but all six double bridges to C are left.

**Attempt 3 (start at R):** R → C (R–C₁) → S (S–C₁) → C (S–C₂) → P (P–C₁) → C (P–C₂) → R (R–C₂) → S → P → Q → C.
Stuck at C after 10 of 11 bridges: only Q–R is left, and I'm nowhere near it.

All three failures ended at a "wrong" island, which made me try counting instead of guessing.

### Bridges touching each island

| Island | Number of bridges |
| ------ | -----------------: |
| P | 4 |
| Q | 3 |
| R | 4 |
| S | 4 |
| C | 7 |

### Possible or impossible?

**Possible.** Exactly two islands have an odd number of bridges touching them: Q has degree 3 and C has degree 7. A connected graph has a walk that uses every bridge exactly once when it has exactly zero or two odd-degree vertices. With two odd-degree vertices, the walk must start at one and finish at the other.

### My walk

One valid walk is:

**C → P → Q → R → S → P → C → R → C → S → C → Q**

This walk uses all 11 bridges exactly once. The two visits along P–C, the two along R–C, and the two along S–C use the separate parallel bridges.

### Why?

Every time a walk enters an island and then leaves it, it uses bridges in pairs. Therefore, an island with an odd number of bridges cannot be both an ordinary middle point and have all its bridges paired up. For a walk using every bridge exactly once, there can be either no odd-degree islands (if it finishes where it started) or exactly two (the start and end islands).

## What surprised me

I was wrong: adding bridges didn't make it harder. The extra bridges turned P, R and S from odd to even, which is what made the walk possible. Also, attempt 3 got within one bridge of finishing just by starting on the wrong island. The start point matters more than the route.

## So I think what's happening is

Every island in the middle of a walk needs bridges in pairs: one in, one out. Only the start and end islands can have a leftover odd bridge. So the walk is possible only when 0 or 2 islands have an odd count, and with 2 you must start at one of them. Mine has exactly two (Q = 3, C = 7), so I start at C and end at Q.

## The pattern being covered here is...

This problem illustrates Euler trails in graph theory: the number of bridges touching each island determines whether a walk can use every bridge exactly once.

## Did I use AI? For what?

Yes. I used AI tools (Claude and another assistant) to help draft this solution: the Enigma number table, the map setup, the counting argument, the attempts and the final walk. I checked the bridge counts and traced the final walk myself to confirm it uses all 11 bridges exactly once.
