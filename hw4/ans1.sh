#!/bin/bash
echo "-----------------------------------------------------------------"
echo "-----------------------------------------------------------------"
echo "Q1: total points: 1.5"
echo "number of lines should be 466." 
echo "given number of lines:"
bash q1.sh | wc -l 
echo "-----------------------------------------------------------------"
echo "first line should be:"
echo "HEADER    TRANSFERASE                             15-OCT-12   4HKD"
echo "Given first line"
bash q1.sh | head -n1
echo "-----------------------------------------------------------------"
echo "last line should be"
echo "SCALE3      0.000000  0.000000  0.004781        0.00000"
echo "Given last line"
bash q1.sh | tail -1
echo "-----------------------------------------------------------------"
