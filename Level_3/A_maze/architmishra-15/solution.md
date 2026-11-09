# 3A: architmishra-15

## My Enigma number

E = 122433. The last digit is 3, so my maze number is 3.

## 3A: The maze where you may break walls

### My maze number and my maze

Maze 3 (S = row 1, col 1; X = row 7, col 7):

```
    1 2 3 4 5 6 7
1   S . . . . # #
2   # . . # . . .
3   . # . . # # #
4   . . . # . # .
5   . # # . # . .
6   . . . # . # #
7   . . . . # . X
```

### My guess (k = 0, k = 1, k = 2)

k = 1: about 16

### k = 0, flooding by hand

Start with 0 in S, then 1 in every open neighbour, and so on. `#` = wall, `?` = open but never reached:

```
     1  2  3  4  5  6  7
1    0  1  2  3  4  #  #
2    #  2  3  #  5  6  7
3    8  #  4  5  #  #  #
4    7  6  5  #  ?  #  ?
5    8  #  #  ?  #  ?  ?
6    9 10 11  #  ?  #  #
7   10 11 12 13  #  ?  ?
```

The flood stops after step 13 at (7,4). The exit X at (7,7) never gets a number, so **there is no path with k = 0**. The wall at (7,5) is what cuts the bottom row off from the exit.

### k = 1, shortest path length and the path

**Shortest length = 16 steps.** Break the wall at (7,5).

`o` = path, `B` = wall broken:

```
    1 2 3 4 5 6 7
1   S o . . . # #
2   # o o # . . .
3   . # o . # # #
4   o o o # . # .
5   o # # . # . .
6   o . . # . # #
7   o o o o B o X
```

Path: (1,1) → (1,2) → (2,2) → (2,3) → (3,3) → (4,3) → (4,2) → (4,1) → (5,1) → (6,1) → (7,1) → (7,2) → (7,3) → (7,4) → **(7,5)** → (7,6) → (7,7).

The detour through the top-left is needed because the wall at (2,1) blocks the straight way down column 1, and the only break is used on (7,5).

### k = 2, shortest path length and the path

**Shortest length = 12 steps.** Break the walls at (2,1) and (7,5).

```
    1 2 3 4 5 6 7
1   S . . . . # #
2   B . . # . . .
3   o # . . # # #
4   o . . # . # .
5   o # # . # . .
6   o . . # . # #
7   o o o o B o X
```

Path: (1,1) → **(2,1)** → (3,1) → (4,1) → (5,1) → (6,1) → (7,1) → (7,2) → (7,3) → (7,4) → **(7,5)** → (7,6) → (7,7).

This is straight down column 1 and straight along row 7. It's 6 + 6 = 12 steps, the smallest possible for a 7×7 grid, so no maze could do better.

### Why "where am I" isn't enough any more

Without breaking, the square you stand on tells you everything about what you can do next. With breaks, two walkers on the same square can be in different situations, because one has used up breaks and the other hasn't. So the state is (square, walls broken so far), which is why we draw floors.

Example in my maze, square (7,4), with k = 1:
- If I arrive with 0 breaks used (floor 0, after 13 steps), I can step onto the wall (7,5) and carry on to X.
- If I had already used my one break earlier, I'm on floor 1 and (7,5) is a wall I can't pass, so I'm stuck.

Same square, different options. Another example: (7,1) is reached at step 10 on floor 0, but at step 6 on floor 1 (by breaking (2,1)). The faster arrival has cost a break, so I can't just keep "the best time" per square.

### Why flooding finds the shortest path

Flooding finds all squares reachable in 1 step, then all squares reachable in 2 steps, and so on, so squares are numbered in order of distance. A square gets its number the first time the flood reaches it, and the flood reaches it at the earliest step when any path could get there. The exit is numbered at the first step when some path reaches it, so that number cannot be beaten by any shorter path (a shorter path would have reached it in an earlier round). With floors, the same argument holds on the (square, floor) states.

## Bonus

- **Smallest k for the 12-step path:** k = 2. With k = 1 the best is 16, and with k = 2 we reach 12, which is the minimum possible.
- **Squares on three floors when k = 2:** 3 × 49 = 147. Each (square, floor) gets numbered at most once, so the flood writes at most 147 numbers, which is still tiny by hand and trivial for a computer.
- **Can one more break make the path longer?** No. Everything allowed with k breaks is still allowed with k + 1 breaks (you just don't have to use the extra one), so the set of possible paths only grows and the shortest length can only stay the same or get shorter. (Here: no path → 16 → 12.)

## What surprised me
My guess for k = 1 was about 16, and that turned out to be exactly right, which I didn't expect. What did surprise me was how much one more break helps after that: going from k = 1 to k = 2 cut the path from 16 to 12 steps, a saving of 4. The first break is what makes the exit reachable at all (k = 0 has no path), but the second one is what lets the path go straight instead of taking the long detour through the top-left. I also hadn't expected a single wall, (7,5), to be the thing blocking the whole maze, and that it is broken in both the k = 1 and k = 2 paths.

## Did I use AI? For what?

I used Claude to crossverify and check my answers, and I planned the answer and the explanations myself.
