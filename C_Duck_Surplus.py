t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    current_max = a[0]
    
    for i in range(1, n):
        if a[i] >= current_max:
           
            current_max = a[i]
        else:
          
            current_max += a[i]
            
    print(current_max)