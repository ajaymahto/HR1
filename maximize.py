K, M = map(int, raw_input().strip().split())
elements = []
for x in range(0, K):
    list1 = raw_input().split()
    N = int(list1[0])
    elements[x] = set(map(int, list1[1:]))
print elements


