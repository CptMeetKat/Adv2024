#!/usr/bin/bash


main()
{
    input=$1
    multiplications=$(cat $input | grep -oP "(?<=mul\()[0-9]*,[0-9]*(?=\))")
    result=0
    while IFS=, read -ra line; do
        result=$((result + (line[0] * line[1])))
    done <<< $multiplications

    echo Result: $result
}

main $1
