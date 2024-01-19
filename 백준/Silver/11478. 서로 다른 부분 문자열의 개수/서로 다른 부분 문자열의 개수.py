def count_substrings(s):
    substrings = set()
    n = len(s)

    for i in range(n):
        for j in range(i + 1, n + 1):
            substrings.add(s[i:j])

    return len(substrings)
s = input().rstrip()
print(count_substrings(s))