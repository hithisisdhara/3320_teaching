#!/bin/sh 
cat $1 | awk '{
sgn = substr($0,1,1);
gsub("-","",$0); 
split($0, a, "/");
val = (a[1]*23+a[2])*17+a[3];
if (sgn == "-") {val = -val};
}{print val}'