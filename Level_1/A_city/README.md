# 1A: The bridges of your city

Part of [Level 1: Observe](../README.md). You need your **Enigma number E** (see the [main README](../../README.md#your-enigma-number-e)). The examples use E = 4671, from the username `math-cat7`.





**What to submit:** one pull request that adds your work to `Level_1/A_city/<your-github-username>/`. Any format is fine: a `solution.md`, a scanned PDF of handwritten pages, or photos of your pages. Keep each file under 2 MB.

---

## The Story

In 1736, the city of Königsberg had seven bridges. People wondered whether you could take a walk that **crosses every bridge exactly once**. Nobody could find one. Euler proved it's impossible, and in doing so started a whole new area of maths, yep, you guessed it :  graph theory.

Now it's your turn, with your own city.

## Your map

Your city has a central island **C** and four outer islands **P, Q, R, S**:

```
          P
        / | \
      S - C - Q
        \ | /
          R
```

Bridges that are always there:

- Each outer island has a bridge to its two neighbours: P–Q, Q–R, R–S, S–P.
- Each outer island has one bridge to the centre: P–C, Q–C, R–C, S–C.

Your Enigma number adds extra bridges:

1. Take the **last 4 digits** of E. If E has fewer than 4 digits, add zeros in front (45 becomes 0045).
2. The 1st digit decides P–C, the 2nd Q–C, the 3rd R–C, the 4th S–C.
3. **If the digit is odd, that bridge gets a second bridge next to it.**

## The rules of the "walk"

- Cross **every bridge exactly once**.
- You can start and finish on any islands you like.
- A double bridge is two separate bridges, and each must be crossed.

## What you do

1. **Draw your map**, including any double bridges. How many bridges are there in total?
2. **Guess:** before trying anything, do you think a walk is possible?
3. **Try:** attempt at least 3 walks by hand. Note where each one got stuck.
4. **Count:** for every island, count how many bridges touch it. Put the counts in a table.
5. **Decide:** if a walk is possible, write it as a list of islands (for example P → C → S → …). If it's impossible, explain why using your counts.
6. **Explain the rule:** why do the counts decide everything?

## Bonus (optional) 



If you guys do all the bonus problems, well then, https://www.youtube.com/watch?v=-xjzG2wPP1M  

- The real Königsberg had 4 pieces of land, with 5, 3, 3 and 3 bridges touching them. Use your rule to explain why Euler said no.
- If your walk is impossible, what's the smallest number of bridges you could add to make it possible, and where?
- Can your walk end on the same island where it started? When is that possible?
- Describe a method for finding the walk that would work on *any* map, not just yours.

---

## What we expect to see

This is a guideline, not a form. Your work should cover these points, in any format. If you write a `solution.md`, these headings make a good outline:

```
# 1A: <your-github-username>

## My Enigma number

E = (show your working)

## 1A: The bridges of your city

My last 4 digits and my map:

My guess:

My attempts:

Bridges touching each island (table):

Possible or impossible:

My walk (if possible):

Why:

## What surprised me 
## So I think whats happening is : 
## The pattern being covered here is... 
## Did I use AI? For what?
```
