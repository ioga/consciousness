#!/bin/bash
declare -A map
map["weather.dat"]='{ print $2-$3, $1; }'
map["football.dat"]='{ print ($7>$9?$7-$9:$9-$7), $2; }'

for key in ${!map[@]}
do
    cat $key | grep '^[[:space:]]*[[:digit:]]' |\
        awk "${map[$key]}" |\
        sort -n | head -n 1 | awk '{ print $2; }'
done
