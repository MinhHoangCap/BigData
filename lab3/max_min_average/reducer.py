#!/usr/bin/python3

import sys
s=0
c=0
(last_key,max_val, min_val, avg_val) = (None,-sys.maxsize, +sys.maxsize,0)
for line in sys.stdin:
  (key, val) = line.strip().split("\t")
  if last_key and last_key != key:
    avg_val=s/c
    print("%s\t%s\t%s\t%s" % (last_key, max_val, min_val, avg_val))
    (last_key,max_val, min_val, avg_val) = (key,int(val), int(val), int(val))
  else:
    (last_key,max_val, min_val, avg_val) = (key, max(max_val,int(val)), min(min_val, int(val)), s+int(val))
    s= avg_val
    c=c+1
if last_key:
  avg_val=s/c
  print("%s\t%s\t%s\t%s" % (last_key, max_val, min_val, avg_val))