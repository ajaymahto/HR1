super_set = set(raw_input().strip().split())
N = int(raw_input().strip())
flag = 0
for x in range(0, N):
    set1 = set(raw_input().strip().split())
    if len(set1) > len(super_set) or len(super_set.intersection(set1)) >= len(super_set) or \
                    not (super_set.intersection(set1) == set1):
        flag = 1
        break
print flag == 0