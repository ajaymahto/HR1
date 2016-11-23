N = int(raw_input().strip())
set1 = set(map(int, raw_input().strip().split()))
n = int(raw_input().strip())
while n > 0:
    command, num = raw_input().strip().split()
    num = int(num)
    set2 = set(map(int, raw_input().strip().split()))
    if command == "intersection_update":
        set1.intersection_update(set2)
    elif command == "update":
        set1.update(set2)
    elif command == "difference_update":
        set1.difference_update(set2)
    elif command == "symmetric_difference_update":
        set1.symmetric_difference_update(set2)
    # print command, num
    # print set2
    # print set1
    n -= 1
s = 0
for num in set1:
    s += num
print s