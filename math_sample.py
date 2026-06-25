def calculate_heavy_sum(limit):
    total = 0
    for i in range(limit):
        total += i
    return total

print("Result:", calculate_heavy_sum(10000000))
