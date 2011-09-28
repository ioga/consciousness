Motivation
====
Extract top k (which is hardcoded at `reducer.py`) hosts from list of urls using MapReduce (hadoop streaming).

Simple usage
===
    cat urls.txt | ./mapper.py | sort | ./reducer.py
