#! /usr/bin/env python

M = int(raw_input().strip())
set1 = set(raw_input().strip().split())
N = int(raw_input().strip())
set2 = set(raw_input().strip().split())

inA = set1.difference(set2)
inB = set2.difference(set1)
for element in sorted(map(int, list(inA.union(inB)))):
	print element