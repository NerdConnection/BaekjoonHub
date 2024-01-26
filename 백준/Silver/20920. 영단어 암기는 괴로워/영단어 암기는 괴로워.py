import sys

n, m = map(int, sys.stdin.readline().split())

dic = {}
for _ in range(n):
    word = sys.stdin.readline().rstrip()
    word_len = len(word)
    if word_len < m:
        pass
    else:
        if dic.get(word) is None:
            dic[word] = 1
        else:
            dic[word] += 1

sorted_keys = sorted(dic.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
for word in sorted_keys:
    print(word[0])

