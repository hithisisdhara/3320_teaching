#!/bin/bash
cat 4HKD.pdb | grep "HOH " | sed s'/HOH/WAT/g'
