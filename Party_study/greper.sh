#!/bin/sh

sat=$1
sun=$2
in_file=$3
out_file=$4

grep "^${sat} 23.*" "$in_file" >> "$out_file"
grep "^${sun} 0[0-6].*" "$in_file" >> "$out_file"