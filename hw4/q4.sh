#!/bin/bash
grep "^ATOM " 4HKD.pdb | awk '
{column7 += $7
column8 += $8
column9 += $9
average7 = column7/NR
average8 = column8/NR
average9 = column9/NR}
END{print "The average value of column 7 is " average7,
 "The average value of column 8 is " average8,
 "The average value of column 9 is " average9}'
