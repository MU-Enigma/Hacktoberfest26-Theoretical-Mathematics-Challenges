# 2A: rks746

## My Enigma number

GitHub username: rks746  
According to the algorithm,  
r = 18  
k = 11  
s = 19  
7,4,6 as they are 

18x1 + 11x2 + 19x4 + 7x8 + 4x16 + 6x32 = 18 + 22 + 76 + 56 + 64 + 192  

Enigma number (E) = 428  

## 2A: Break the Enigma number

Does another username shares my Enigma number?  
My guess: Yes

### Twin 1
The numbers in the username can be replaced with equivalent alphabets.  
So, rks746 becomes  
rksgdf since (g = 7, d = 4 and f = 6)

Check:-  
E of rksgdf  
= 18x1 + 11x2 + 19x4 + 7x8 + 4x16 + 6x32  
= 18 + 22 + 76 + 56 + 64 + 192  
= 428 = E of rks746

### Twin 2
Since addition is commutative, the order doesn't matter.  
The position values remain fix.  
So we only have to make sure the "sum" is as desired. 

Sum of r and k in rks746 is  
= 18x1 + 11x2  
= 18 + 22  
= 40

Replacing r with j and k with o, the sum is  
= 10x1 + 15x2  
= 10 + 30  
= 40  
Hence, jos746 and rks746 have same E.

Similar thing can be applied to the digits.  
Sum of 746 is  
= 7x8 + 4x16 + 6x32  
= 56 + 64 + 192  
= 312

Replacing 746 with 765 in the same positions, the sum is  
= 7x8 + 6x16 + 5x32  
= 56 + 96 + 160  
= 312  
Hence, rks746 and rks765 have the same E.

### The two reasons for collisions:
1. Addition is commutative, so order of individual units and there quantity may not affect the sum.  
If (axb + cxd) and (pxb + qxd) give the same sum, both usernames will have same E, even though the characters of both usernames, ac and pq, are different. 

2. Another reason why collisions occur is because some characters share common values, 'a' has value 1 and 1 has value 1. Each character needs a unique value to avoid collisions. 

### My new rule 
Current rule for calculating enigma value is quite straightforward.  
Letters have values as they occur in the alphabet series 
a = 1, b = 2, ... z = 26  
Digits have their numerical values.  
Each character is multiplied with 2^p, where p is its position, and summed to calculate Enigma value (E).

Another method would involve assigning unique values to each character.  
a to z get assigned values from 1 to 26  
0 to 9 get assigned values from 27 to 36  
"-" is of value 37  

New rule would involve multiplying each character value with 38^(n-p)  
where n = total number of characters in username and p is the position of that character.  

So, for username rks746  
E = 18x(38^(6-1)) + 11x(38^(6-2)) + 19x(38^(6-3)) + 34x(38^(6-4)) + 31x(38^(6-5)) + 33x(38^(6-6))   
E = 1,450,262,395  

The Enigma number is significantly large, a trade-off for unique representation. 

### Proof that it never collides 
Given 2 usernames U and V  
If E(U) = E(V),  
we have to prove that U = V. 

Given, E(U) = E(V)  
Basically, E = sum(value of character x 38^(n-p))  
If U and V are same length, all the 38^(n-p) values will be the same.  
Then for E(U) = E(V), all character values also should be equal.  
Since, it is guarenteed that all characters have unique values, all the characters should also be same.  
Thus, for E(U) to be equal to E(V), U = V. 

### What surprised me?
The fact that changing the base from 2 to 38-base encoding could solve the collision issue is what surprised me the most. 

### Who helped me?
I used AI for the new rule idea and proof that it never allows collision.