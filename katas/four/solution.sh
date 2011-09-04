#!/bin/bash
declare -A map # map data filenames to column number for awk code
map["weather.dat"]='-v p=2 -v q=3 -v r=1'
map["football.dat"]='-v p=7 -v q=9 -v r=2'

awk_program='{ print abs($p - $q), $r; } function abs(val) { return val>0?val:-val; }'

for key in ${!map[@]}
do
    grep '^[[:space:]]*[[:digit:]]' $key |\
        awk ${map[$key]} "$awk_program" |\
        sort -n | head -n 1 | cut -d ' ' -f 2
done
