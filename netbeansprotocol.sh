#!/bin/bash

url=$2
file=${url#*\/\/}
file=${file%?line=*}
line=${url#*line=}

/home/robo47/netbeans-7.0/bin/netbeans --open $file:$line
