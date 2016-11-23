n = int(raw_input().strip())
set1 = set(map(int, raw_input().strip().split()))
N = int(raw_input().strip())
while N > 0:
    op = raw_input().strip()
    if op == "pop":
        set1.pop()
    else:
        op1, num = op.split()
        num = int(num)
        if op1 == "remove":
            set1.remove(num)
        elif op1 == "discard":
            set1.discard(num)
    N -= 1
s = 0
for num in set1:
    s += num
print s
