#!/usr/bin/env python
"""Extract hostname from url"""

import sys
from urlparse import urlsplit

for line in sys.stdin:
    hostname = urlsplit(line.strip()).hostname
    if hostname:
        print '%s\t%s' % (hostname, 1)
