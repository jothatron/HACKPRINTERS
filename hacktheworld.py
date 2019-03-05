#!/bin/bash
while read -r line; do
    ip="$line"
    ./PRET/pret.py $ip pjl -q -i ./commands.txt
done < "./iplist.txt"
