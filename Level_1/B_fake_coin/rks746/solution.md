# 1B: rks746

## My Enigma Number 

GitHub username: rks746  
According to the algorithm,  
r = 18  
k = 11  
s = 19  
7,4,6 as they are 

18x1 + 11x2 + 19x4 + 7x8 + 4x16 + 6x32 = 18 + 22 + 76 + 56 + 64 + 192  

Enigma number (E) = 428  

## 1B: Find the fake coin

n = 10 + (remainder of E ÷ 90)
    = 10 + 68
    = 78

### My guess for 27 coins 
First divide it into 2 groups - 13 and 13. And keep one coin aside.  
If both 13 coins balance, then the one coin left is fake (best case scenario)

If unbalanced, the heavier side contains fake coin. 
13 divides into 6+6+1 and so on

27->13->6->3->1, 4 weighings required


### Halving (worst case)
By halving,  
27->13->6->3->1,  
4 weighings are required in the worst case.  

### Table
| No of coins | Fewest weighings |
| :---: | :---: |
| 2 | 1 |
| 3 | 1 |
| 4 | 2 |
| 5 | 2 |
| 6 | 2 |
| 7 | 2 |
| 8 | 2 |
| 9 | 2 |
| 10 | 3 |
| 11 | 3 |
| 12 | 3 |
| 13 | 3 |
| 14 | 3 |
| 15 | 3 |
| 16 | 3 |
| 17 | 3 |
| 18 | 3 |
| 19 | 3 |
| 20 | 3 |
| 21 | 3 |
| 22 | 3 |
| 23 | 3 |
| 24 | 3 |
| 25 | 3 |
| 26 | 3 |
| 27 | 3 |

### Rule folowed for filling the table
k = ceiling[log n base 3]  
where n = no of coins and k = minimum no of weighings required  
Thus, this formula is better than halving the stack of coins. 

### Prediction for n
n = 78  
So k = 4

### Weighing plan 
78 = 26 + 26 + 26 (1st weighing)  
One of the 3 groups will have the fake coin which can be found out in 1 weighing.

26 = 9 + 9 + 8 (2nd weighing)  
If group with 9 coins weigh equal, fake coin is in the one with 8 coins.
Else, fake coin is in the group of 9 which is heavier. 

9 = 3 + 3 + 3 or 8 = 3 + 3 + 2 (3rd weighing)

Worst case: 3 = 1 + 1 + 1 (4th weighing)  
Guarenteed to find fake coin in 4 weighings.

### Why dividing into 3 beats 2?
Dividing into 3 groups means removing 1/2 coins per weighing.   
Dividing into 3 groups means removing 2/3 coins per weighing. Hence it is better.

### Why no plan can do better
My plan finds fake coin in 4 weighings. A better plan would do it in 3 or less weighings.  
3 weighings can find fake coin in a stack at max having 27 coins (3^3), which is less than 78.  
So, atleast 4 weighings are needed in this case. 

### What suprised me
The fact that halving the stack into 2 groups is not the most efficient approach surprised me the most. Dividing into 3 groups is a far better approach.

## Bonus 

### When 12 coins present 
1 coin is fake  
Fake coin might be heavier or lighter than the originals.  
So now, if the scale bends towards a certain side, it might be because that side contains a heavier fake coin or the other side  has a lighter fake coin.  

Approach 1  
Divide into 3 groups.  
4 + 4 + 4 (1 weighting)  
2 groups out of the 3 are guarenteed to be equal (since there is only one fake coin). That can be found out in at max 3 weighings since we don't know whether fake coin is heavier or lighter.  
That would take a total of 5 weighings, but 5>3.

But it is possible in 3 weighings since (3^3) > (12x2).  

Approach 2  
Weighing 1: 1,2,3,4 vs 5,6,7,8

If they are balanced,  
Fake is among 9,10,11,12.  

Weighing 2: 9,10,11 vs 1,2,3

If (9,10,11) > (1,2,3), then fake coin is heavier than original coin (one more weighing needed to find out which among 9,10,11 is fake)

If (9,10,11) < (1,2,3), then fake coin is lighter than original coin (one more weighing needed to find out which among 9,10,11 is fake)

If (9,10,11) = (1,2,3), then fake coin is 12.

Even if 1,2,3,4 vs 5,6,7,8 are not balanced, similar strategy can help find the fake coin in 3 weighings.

### When there are 14 coins.
The fake coin can either be heavier or lighter than the original coin.  
So there are 14x2 = 28 possibilities.  
The max stack for 3 weighings is 3^3 = 27<28. So, 3 weighings can't handle 14 coins. 

### Who helped me?
I used AI for finding the k = ceiling[log n base 3] formula and understanding how dividing into 3 groups actually works. Also used AI to understand the bonus question solution.
