def get_steps_and_gcd(a, b):
    steps = 0
    while b > 0:
        steps += 1
        # a % b is the leftover piece after cutting the largest possible squares
        a, b = b, a % b
    return steps, a

def find_top_pairs(n, top_k=10):
    results = []
  
    for a in range(1, n + 1):
        for b in range(1, a + 1):
            steps, gcd = get_steps_and_gcd(a, b)
            results.append(((a, b), steps, gcd))
            
    # Sort primarily by steps (descending), then by 'a' to break ties consistently
    results.sort(key=lambda x: (x[1], x[0][0], x[0][1]), reverse=True)
  
    print(f"Top {top_k} pairs by number of steps (N={n}):\n")
    print(f"{'Pair (a, b)':<15} | {'Steps':<7} | {'GCD'}")
    print("-" * 35)
    
    for i in range(min(top_k, len(results))):
        pair, steps, gcd = results[i]
        print(f"{str(pair):<15} | {steps:<7} | {gcd}")

n = 33
find_top_pairs(n)
