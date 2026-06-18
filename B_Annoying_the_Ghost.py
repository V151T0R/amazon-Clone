
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    
    used = [False] * n
    assignment = [-1] * n  
    
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
    
    # Counting the  inversions in assignment array
    inv = 0
    for i in range(n):
        for j in range(i+1, n):
            if assignment[i] > assignment[j]:
                inv += 1
    
    print(inv)