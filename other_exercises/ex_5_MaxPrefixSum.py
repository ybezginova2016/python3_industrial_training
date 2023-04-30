def get_max_prefix_sum(arr):
    maximal_sum = 0
    for i in range(1, len(arr)+1):
        current_sum = sum(arr[0:i])
        maximal_sum = max(maximal_sum, current_sum)
    return maximal_sum

x = [1, 6, 4]
print(get_max_prefix_sum(x))