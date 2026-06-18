import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    # Each a[i] must be assigned to some b[j] where b[j] >= a[i]
    # We want to find assignment that minimizes inversions
    # Greedy: assign each a[i] to smallest possible b[j] >= a[i]
    
    # For each a[i], find all valid b[j] (b[j] >= a[i])
    # Then find assignment minimizing inversions (= adjacent swaps)
    
    # Key insight: assign greedily - for each a[i], pick smallest b[j] >= a[i]
    # Then count inversions in the resulting permutation of indices
    
    used = [False] * n
    assignment = [-1] * n  # assignment[i] = index in b that a[i] maps to
    
    valid = True
    for i in range(n):
        best = -1
        for j in range(n):
            if not used[j] and b[j] >= a[i]:
                if best == -1 or b[j] < b[best]:
                    best = j
        if best == -1:
            valid = False
            break
        assignment[i] = best
        used[best] = True
    
    if not valid:
        print(-1)
        continue
    
    # Count inversions in assignment array
    inv = 0
    for i in range(n):
        for j in range(i+1, n):
            if assignment[i] > assignment[j]:
                inv += 1
    
    print(inv)