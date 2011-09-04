#!/usr/bin/env python
"""Get top k hosts"""

import sys
from itertools import groupby
from heapq import heappush, heappushpop

heap = []
k = 5

def rheapadd(heap, item):
    if len(heap) >= k:
        heappushpop(heap, item)
    else:
        heappush(heap, item)

def main():
    data = (line.strip().split('\t', 1) for line in sys.stdin)
    for host, g in groupby(data, lambda p: p[0]):
        s = 0
        for h, count in g:
            try: s += int(count)
            except ValueError: continue
        rheapadd(heap, (s, host))
    for count, host in sorted(heap, reverse=True):
        print '%s\t%s' % (host, count)

if __name__ == "__main__":
    main()
