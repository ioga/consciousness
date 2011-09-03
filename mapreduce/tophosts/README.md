Motivation
====
Extract top k hosts from list of urls using MapReduce (hadoop streaming).

Simple usage
===
    cat urls.txt | ./mapper.py | sort | ./reducer.py
