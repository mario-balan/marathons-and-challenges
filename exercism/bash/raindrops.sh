#!/usr/bin/env bash

main () {
if [ $(($1 % 3)) -eq 0 ]; then
    rain+="Pling"
fi

if [ $(($1 % 5)) -eq 0 ]; then
    rain+="Plang"
fi

if [ $(($1 % 7)) -eq 0 ]; then
    rain+="Plong"
fi

if [[ -z "${rain}" ]]; then
    rain=$1
fi

printf "$rain\n"
}

main "$@"

# A neat and compact alternative:
# [ $(($1 % 3)) -eq 0 ] && rain+=Pling
# [ $(($1 % 5)) -eq 0 ] && rain+=Plang
# [ $(($1 % 7)) -eq 0 ] && rain+=Plong
# printf "${rain:-$1}\n"
