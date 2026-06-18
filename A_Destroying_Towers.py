
t = int(input())

for _ in range(t):
    n = int(input())
    H = list(map(int, input().split()))
    
    total_sum = 0
    current_min = float('inf')
    
    # Process each tower's height
    for height in H:
        # Update the lowest height seen so far
        if height < current_min:
            current_min = height
            
        
        total_sum += current_min
        
    print(total_sum)