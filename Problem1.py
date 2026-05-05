def max_cyclic_sum(s):
    n = len(s)
    s = s + s

    seen = set()
    left = 0
    curr = 0
    max_sum = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            curr -= (ord(s[left]) - ord('a') + 1)
            left += 1

        seen.add(s[right])
        curr += (ord(s[right]) - ord('a') + 1)

        if right - left + 1 <= n:
            max_sum = max(max_sum, curr)

    return max_sum


s = input().strip()
print(max_cyclic_sum(s))