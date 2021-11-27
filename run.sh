#!/bin/bash

if [ $# -eq 0 ];
then
    poetry run python -m yavpm
else
    cmd="poetry run python -m yavpm"
    for arg in "$@"
    do
        cmd="$cmd $arg"
    done
    eval $cmd
fi
