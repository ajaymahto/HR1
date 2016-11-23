#! /usr/bin/env python

from collections import Counter as counter

M, N = map(int, raw_input().strip().split())
my_set = raw_input().strip().split()
freq = counter(my_set)
my_unique_set = list(set(my_set))
set1 = raw_input().strip().split()
set2 = raw_input().strip().split()

happyness = 0
for number in set1:
	if number in my_unique_set:
		happyness += freq[number]

for number in set2:
	if number in my_unique_set:
		happyness -= freq[number]

print happyness