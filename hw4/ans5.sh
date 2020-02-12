echo "Q5: pts 0.5"
echo "-----------------------------------------------------------------"
echo "please delete the file3 if exists"
echo "Total number of lines in file3 should be 1164 and the lines containing HOH should be 0"
bash q5.sh
echo "Number of lines in file3"
cat file3 | wc -l 
echo "the number of lines in file3 having HOH"
cat file3 | grep "HOH" |wc -l
echo "-----------------------------------------------------------------"
