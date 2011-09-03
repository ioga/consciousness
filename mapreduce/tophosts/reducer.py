#!/usr/bin/env python
"""Get top k hosts"""

import sys
from heapq import heappush, heappushpop

current_host = None
current_count = 0
host = None

heap = []
k = 5

def rheapadd(heap, item):
    if len(heap) >= k:
        heappushpop(heap, item)
    else:
        heappush(heap, item)

for line in sys.stdin:
    host, count = line.strip().split('\t', 1)

    try:
        count = int(count)
    except ValueError:
        continue
    if current_host == host:
        current_count += count
    else:
        if current_host:
            rheapadd(heap, (current_count, current_host))
        current_count = count
        current_host = host

if current_host == host:
    rheapadd(heap, (current_count, current_host))

for count, host in sorted(heap, reverse=True):
    print '%s\t%s' % (host, count)
