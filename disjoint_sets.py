#! /usr/bin/env python

M, N = map(int, raw_input().strip().split())
set1 = raw_input().strip()
set2 = raw_input().strip()
my_set = raw_input().strip()
my_unique_set = list(set(my_set.split()))

happyness = 0
for number in my_unique_set:
	if number in set1:
		happyness += my_set.count(number) 
	elif number in set2:
		happyness += (-1 * my_set.count(number))
print happyness