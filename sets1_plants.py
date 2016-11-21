#! /usr/bin/env python
from __future__ import division

N = int(raw_input().strip())
plants = map(int, raw_input().strip().split())
distinct_plants = list(set(plants))
#print distinct_plants

print "%.3f" % (sum(map(int, distinct_plants)) / len(distinct_plants))
#print "%.3f" % (sum(map(int, distinct_plants)) / (len(distinct_plants) * 1.0))