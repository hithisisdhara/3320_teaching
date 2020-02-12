#!/bin/bash/
echo -n "Column 7 min = "
grep "^ATOM " 4HKD.pdb | sort -nk7 | head -n1 | awk '{print $7}'
echo -n "Column 7 max = "
grep "^ATOM " 4HKD.pdb | sort -nk7 | tail -1 | awk '{print $7}'
echo -n "Column 8 min = "
grep "^ATOM " 4HKD.pdb | sort -nk8 | head -n1 | awk '{print $8}'
echo -n  "Column 8 max = "
grep "^ATOM " 4HKD.pdb | sort -nk8 | tail -1 | awk '{print $8}'
echo -n "Column 9 min = "
grep "^ATOM " 4HKD.pdb | sort -nk9 | head -n1 | awk '{print $9}'
echo -n  "Column 9 max = "
grep "^ATOM " 4HKD.pdb | sort -nk9 | tail -1 | awk '{print $9}'

