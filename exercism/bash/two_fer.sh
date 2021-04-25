#!/usr/bin/env bash

# The solution I first came up with:
#
# NAME=$1
#
# if [ -z "$1" ]; then
#     echo "One for you, one for me."
# else
#     echo "One for $NAME, one for me."
# fi

# The solution after learning about defaulting in bash variables:

printf "One for ${1:-you}, one for me.\n"
