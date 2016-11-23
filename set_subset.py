t = int(raw_input().strip())
for x in range(0, t):
    a = int(raw_input().strip()); A = set(map(int, raw_input().strip().split()))
    b = int(raw_input().strip()); B = set(map(int, raw_input().strip().split()))
    print "False" if a > b else (A.intersection(B) == A)