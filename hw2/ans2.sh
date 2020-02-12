echo "Q2 total points: 1"
echo "Please delete file2 if exists in this folder"
bash q2.sh
echo "-----------------------------------------------------------------"
echo "Total number of lines in file2: either 32 or 1164"
echo "Given number of lines in file2:"
cat file2 | wc -l 
echo "-----------------------------------------------------------------"
echo "if lines == 32, then The following should match at all indents"
echo "ATOM    129  N   MET A 450      -4.523  16.830 119.280  1.00 14.88           N "
echo "his output"
cat file2 | head -1
echo "___________"
echo "If lines == 1164, the following should be zero:"
echo "his asnwer"
cat file2 | grep "HETATM" | grep "MSE" | wc -l 
echo "-----------------------------------------------------------------"
