#!/bin/bash

url=$1
file=${url#*\/\/}
file=${file%?line=*}
line=${url#*line=}

/home/robo47/netbeans-7.0.1/bin/netbeans --open $file:$line
