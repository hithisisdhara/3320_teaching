#!/bin/bash
 cat 4HKD.pdb | grep "HETATM" | grep "MSE" | sed 's/HETATM/ATOM  /g' | sed 's/MSE/MET/g'

 
