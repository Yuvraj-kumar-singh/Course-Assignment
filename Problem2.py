def min_operations(arr, k):
    for i in range(1, len(arr)):
        if (arr[i] - arr[0]) % k != 0:
            return -1

    arr.sort()
    median = arr[len(arr) // 2]

    ops = 0
    for x in arr:
        ops += abs(x - median) // k

    return ops


n = int(input())
arr = list(map(int, input().split()))
k = int(input())

print(min_operations(arr, k))