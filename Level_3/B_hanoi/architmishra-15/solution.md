# 3B: architmishra-15

## My Enigma number

E = 122433 (given). The last digit is 3, so E is odd, which means my target is **peg B** (the middle peg).

## 3B: Tower of Hanoi with a broken peg

### Warm-up (classic): moves for 1, 2, 3 disks, and the rule

Any move between any two pegs is allowed, A → C:

| Disks | Moves | Count |
| ----- | ----- | ----- |
| 1 | disk 1: A→C | 1 |
| 2 | disk 1: A→B, disk 2: A→C, disk 1: B→C | 3 |
| 3 | disk 1: A→C, disk 2: A→B, disk 1: C→B, disk 3: A→C, disk 1: B→A, disk 2: B→C, disk 1: A→C | 7 |

Counts: 1, 3, 7. **Rule: 2ⁿ − 1.**

Why, using MOVE: moving n disks uses MOVE(n−1) twice (once to clear the top n−1 disks out of the way, once to put them back) plus one move for the biggest disk. So moves(n) = 2·moves(n−1) + 1. Starting from moves(0) = 0 this gives 1, 3, 7, 15, … = 2ⁿ − 1.

### My target (B or C) and why

E = 122433 is odd, so the target is **B**.

### My guess for 3 disks

(Write your own guess here before reading the rest, for example "about 13".)

### My moves for 1, 2 and 3 disks (every move listed)

Only A↔B and B↔C are allowed. Target: all disks on B.

**1 disk: 1 move**
1. disk 1: A→B

**2 disks: 4 moves**
1. disk 1: A→B
2. disk 1: B→C
3. disk 2: A→B
4. disk 1: C→B

**3 disks: 13 moves**
1. disk 1: A→B
2. disk 1: B→C
3. disk 2: A→B
4. disk 1: C→B
5. disk 1: B→A
6. disk 2: B→C
7. disk 1: A→B
8. disk 1: B→C
9. disk 3: A→B
10. disk 1: C→B
11. disk 1: B→A
12. disk 2: C→B
13. disk 1: A→B

Moves 1–8 take disks 1 and 2 from A to C, move 9 takes disk 3 to B, and moves 10–13 take disks 1 and 2 from C to B.

I also needed the full trip A → C (the tip in the brief). That needs 2, 8 and 26 moves for 1, 2 and 3 disks.

### My bent recursive method

Two methods, because the middle peg changes what "move" means. Here `from` and `to` are the two **end** pegs (A and C in some order), and `B` is always the middle peg.

```
SWING(n, from, to):                      end peg -> other end peg
    if n == 0: stop
    SWING(n - 1, from, to)               top n-1 disks go to the far end
    move disk n from "from" to B
    SWING(n - 1, to, from)               top n-1 disks come back to the start end
    move disk n from B to "to"
    SWING(n - 1, from, to)               top n-1 disks go to the far end again

TO_MIDDLE(n, from):                      end peg -> B   (this is my target)
    if n == 0: stop
    let other = the end peg that is not "from"
    SWING(n - 1, from, other)            top n-1 disks go to the other end peg
    move disk n from "from" to B
    TO_MIDDLE(n - 1, other)              top n-1 disks come to B, onto disk n
```

To solve my task: `TO_MIDDLE(n, A)`.

Move counts:
- S(n) for SWING: S(n) = 3·S(n−1) + 2, with S(0) = 0, so **S(n) = 3ⁿ − 1** (2, 8, 26, 80, …).
- M(n) for TO_MIDDLE: M(n) = S(n−1) + 1 + M(n−1) = 3ⁿ⁻¹ + M(n−1), with M(0) = 0, so **M(n) = (3ⁿ − 1)/2** (1, 4, 13, 40, …).

### My prediction for 4 disks and 10 disks

| Disks | A → B (my target) | A → C |
| ----- | ----------------- | ----- |
| 4 | (81 − 1)/2 = **40** | 81 − 1 = 80 |
| 10 | (59049 − 1)/2 = **29 524** | 59049 − 1 = 59 048 |

The 4-disk plan: SWING(3, A, C) (26 moves), then disk 4: A→B, then TO_MIDDLE(3, C) (13 moves). 26 + 1 + 13 = 40.
The 10-disk plan has the same shape: 3⁹ − 1 = 19 682, plus 1, plus M(9) = 9841, which gives 29 524.

(I also checked my method by computer: it gives legal move sequences for 1 to 10 disks, and a breadth-first search over all arrangements finds the same minimum counts, 1, 4, 13, 40 for A→B and 2, 8, 26, 80 for A→C, for 1 to 4 disks.)

### Why my method is correct

- **Legal moves:** SWING and TO_MIDDLE only ever move a disk A↔B or B↔C, never A↔C. A disk is moved only when all the smaller disks are on a *different* peg, so the biggest disk in play never lands on a smaller one.
- **SWING works:** to take disk n from one end to the other it must pass through B. For disk n to leave "from", the n−1 smaller disks must be on the *other* end ("to"), not on B (disk n is going there) and not on "from". So SWING first moves them to "to". After disk n reaches B, they must be on "from" for disk n to continue to "to", so they swing back. Then disk n goes B → "to", and they swing once more onto it.
- **TO_MIDDLE works:** disk n goes A → B in one step, which needs the other n−1 disks on C. So they go to C first with SWING, then after disk n lands on B they move to B, again from an end peg to the middle, which is TO_MIDDLE(n−1).
- Every call uses a smaller number of disks, so it ends at n = 0.

### Why no plan can do it in fewer moves

Take SWING (A → C). Disk n has to move A→B and then B→C, so at least twice. Before the first move, all n−1 smaller disks must be on C (a full trip of n−1 disks A→C). Before the second, they must be on A (a trip C→A), and after it they must get to C again (a third trip). So at least 3 trips of n−1 disks plus 2 moves of disk n: L(n) ≥ 3·L(n−1) + 2, which is exactly my S(n).
For TO_MIDDLE, disk n moves A→B at least once, and before that all n−1 smaller disks must be on C (a full A→C trip), and afterwards they must get from C to B. That gives M(n) ≥ S(n−1) + 1 + M(n−1), which matches my count.

## Bonus

**All arrangements for 3 disks, A → C (26 moves).** Written as `A | B | C`, bottom to top, `-` means empty:

```
 0: 321 | -   | -
 1: 32  | 1   | -
 2: 32  | -   | 1
 3: 3   | 2   | 1
 4: 3   | 21  | -
 5: 31  | 2   | -
 6: 31  | -   | 2
 7: 3   | 1   | 2
 8: 3   | -   | 21
 9: -   | 3   | 21
10: -   | 31  | 2
11: 1   | 3   | 2
12: 1   | 32  | -
13: -   | 321 | -
14: -   | 32  | 1
15: 2   | 3   | 1
16: 2   | 31  | -
17: 21  | 3   | -
18: 21  | -   | 3
19: 2   | 1   | 3
20: 2   | -   | 31
21: -   | 2   | 31
22: -   | 21  | 3
23: 1   | 2   | 3
24: 1   | -   | 32
25: -   | 1   | 32
26: -   | -   | 321
```

That is 27 arrangements (the start plus 26 moves), all different. The total number of possible arrangements of 3 disks is 3³ = 27, because each disk is on A, B or C and the order on a peg is forced. So the A→C solution visits **every** arrangement exactly once. (Notice step 13: all three disks are on B, which is the A→B target, reached halfway through.)

**Compare the targets.** A→C takes 3ⁿ − 1 moves and A→B takes (3ⁿ − 1)/2, so A→C needs exactly **twice** as many moves as A→B. This matches the list above: the A→C solution passes through "all disks on B" at exactly its halfway point (move 13 of 26), and the second half is the mirror image of the first.

**Why no plan can be shorter:** see the argument above. The biggest disk forces a full trip of all smaller disks each time it has to move.

## What surprised me

What surprised me most was that the 3-disk solution from A to C passes through every one of the 27 possible arrangements exactly once. I expected a shortest plan to skip most of them, but here nothing is wasted and nothing is repeated. I also didn't expect "all disks on B" to appear exactly halfway through the A to C solution, which is why getting to B takes exactly half as many moves as getting to C. Finally, the numbers grow much faster than in the classic puzzle. The classic puzzle needs 2ⁿ − 1 moves, but with the broken peg it is 3ⁿ − 1, so 10 disks need 59 048 moves to reach C and 29 524 to reach B, instead of 1 023.

## Did I use AI? For what?

Proof Checking.
