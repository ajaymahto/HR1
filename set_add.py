N = int(raw_input().strip())
set1 = set()
while N > 0:
    str1 = raw_input()
    set1.add(str1)
    N -= 1
print len(set1)