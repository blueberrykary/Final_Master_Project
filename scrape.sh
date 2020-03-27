#!/bin/bash
truncate -s 0 plist

counter=1
while [ $counter -le 11 ]
do
  lynx -dump https://www.csudh.edu >> plist
  ((counter++))
done
cat plist |grep -Eo ‘[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\:[0-9]{1,5}’
