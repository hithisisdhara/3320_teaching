#!/bin/bash
cat 4HKD.pdb | grep -v ^ATOM\|^CONECT\|^HETATM\|^TER\|^END 4HKD.pdb 
