#!/usr/bin/env bash

dirty=$1 # <---- just here for better readability;
clean="${dirty//[^a-zA-Z\']/ }" # <----- the \' is a post testing ad hoc
upper="${clean^^}" # <---- so we can print without using a new variable

for i in $upper; do
    printf "${i:0:1}" # <------ printf doesn't do CRLF;
done
#printf "\n" # <---- not actually needed (uncomment for prettier outputs)