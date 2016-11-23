from collections import Counter
n = int(raw_input().strip())
list1 = raw_input().strip().split()
count = Counter(list1)
print [num for num in count if count[num] == 1][0]
