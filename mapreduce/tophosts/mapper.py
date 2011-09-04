#!/usr/bin/env python
"""Extract hostname from url"""

import sys
from urlparse import urlsplit

def main():
    for s in (line.strip() for line in sys.stdin):
        hostname = urlsplit(s).hostname
        if hostname:
            print '%s\t%s' % (hostname, 1)

if __name__ == "__main__":
    main()
