#!/usr/bin/bash


main()
{
    input=$1
    multiplications=$(cat $input | grep -oP '((?<=mul\()[0-9]*,[0-9]*(?=\))|do\(\)|don\x27t\(\))')

    disabled=0
    result=0
    while IFS=, read -ra line; do

        if [ ${line[0]} = "don't()" ]; then
            disabled=1
        elif [ ${line[0]} = "do()" ]; then
            disabled=0
        else
            if [ ${disabled} -eq 0 ]; then
                result=$((result + (line[0] * line[1])))
            fi
        fi

    done <<< $multiplications

    echo Result: $result
}

main $1
