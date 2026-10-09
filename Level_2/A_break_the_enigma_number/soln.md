# 2A: architmishra-15

## My Enigma Number: 122433

My Guess: **Collision would indeed occur**

## Working -

We can prove that collision would occur by the Piegon Hole Principle
Let's see the math -

**Max length of GitHub username:** 39

**Total number of allowed characters:** $26 + 10 + 1 = 37$ (only letters, numbers, and hyphens are considered)

$\therefore \text{Total number of possible GitHub usernames} = 37^{39}$

---
The highest possible Enigma Number would be reached when someone keeps z 37 times (highest values letter).

The highest possible Enigma Number would be reached if a username consisted entirely of `z` (the highest value character, 26) for the absolute maximum length of 39 characters.

**Highest Possible Enigma Number:** $E_{max} = \sum_{i=0}^{38} 26 \cdot 2^i = 26 \cdot (2^{39} - 1) \approx 1.43 \times 10^{13}$

**Conclusion by the Pigeonhole Principle:**
Because the number of possible usernames (the pigeons: $37^{39}$) is astronomically larger than the number of possible Enigma numbers (the holes: $\approx 1.43 \times 10^{13}$), multiple usernames are mathematically guaranteed to map to the same Enigma number.

---
### Twin 1 (and its E, worked out):

Let's take the top few letters of my username as an example -

a: $1 \times 1 = 1$
r: $18 \times 2 = 36$
c: $3 \times 4 = 12$
h: $8 \times 8 = 64$
i: $9 \times 16 = 144$  
t: $20 \times 32 = 640$

- Let's take the first two for example: `a` (1) & `r` (18)
- Total value = 37
- Replace the value of `a` and `r` with letters which gives the same sum. Here we can take `c` (3) and `q` (17)
$(3 \times 1) + (17 \times 2) = 3 + 34 = 37$.

$\therefore$ **The first twin name:** ***cqchitmishra-15***

### Twin 2:

- Using the steps as above, let's take third and fourth letters, i.e., `c` (3) and `h` (8)
- Let's replace the values of `c` and `h` with letters which gives the same sum. Here we can take `e` (5) and `g` (7)
- Original Sum: ($3 \times 4) + (8 \times 8) = 76$
- New Sum: ($5 \times 4) + (7 \times 8) = 76$.

Reasons: Already given

## My new rule
To avoid collision, we need the same holes as the number of pigeons, i.e., the same number of max possible hashes (numbers) as there are possible GitHub usernames.
Instead of multiplying it by $2^n$, we can multiply it by $37^n$.

Why it can never collide:

Because if peigon hole principle, it is mathematically guaranteed to not collide.
## What surprised me
I was able to apply Piegon Hole Principle in the first go, lol.
## Did I use AI? For what?
Nope, I did not used AI for this task :)


