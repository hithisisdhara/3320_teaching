
#!/bin/sh 
echo| awk '{print "hi"}'
echo | awk '{a = "hi"; print a}'
echo | awk '{a = “hi”}{print a}'
echo -e "a b c \n d e f" | awk '{print $0}'
echo -e "a b c \n d e f"| awk '{print $1}'
echo -e "a b c \n d e f"| awk '{print $3}'
echo -e "a/b/c \nd/e/f"| awk '{gsub("/", "-",$0); print}'
echo -e "a/b/c \nd/e/f"| awk '{split($0, dhara, "/"); print dhara[1],dhara[2],dhara[3]}'
echo -e "-1/2/0 \n4/5/6" | awk '{print substr($0,1,2)}'
echo -e "-1/2/0 \n4/5/6" | awk '{dhara = substr($0,1,1);print dhara}'
echo "Dhara" | awk '{str1 = substr($0,1,1); str2 = "Initial:" }{ print str2 str1}'
echo -e "-3\n4"| awk '{
sign = substr($0,1,1);
if (sign == "-")
{print $0 " is a negative number"} 
else 
{print $0 " is a positive number"}
}'