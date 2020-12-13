target = int(input())
busses = [int(i) for i in input().split(",") if i != "x"]

best_delta = int(1e9)
best_buss = -1
for buss in busses:
    count = 0
    while count < target:
        count += buss
    
    if count - target < best_delta:
        best_delta = count - target
        best_buss = buss

print(best_buss * best_delta)
