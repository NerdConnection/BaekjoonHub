import sys

while True:
    try:
        n = int(sys.stdin.readline())
        if n == 0:
            print('-')
        else:
            lines = ['-']
            for i in range(1,n+1):
                lines.append(lines[i-1]+' '*(len(lines[i-1]))+lines[i-1])
            print(lines[n])
        
    except:
        break