#!/usr/bin/env bash

# declaring regular vars for readability purposes:
a=$1
b=$2

if [ "$#" -ne 2 ]; then
    echo "Usage: hamming.sh <string1> <string2>"
    exit 1
elif [ ${#a} -ne ${#b} ]; then
    echo "left and right strands must be of equal length"
    exit 1
else
    for ((i = 0; i < ${#a}; i++)); do
        [ "${a:i:1}" == "${b:i:1}" ] || ((diff++))
    done
    echo "${diff:-0}"
fi
