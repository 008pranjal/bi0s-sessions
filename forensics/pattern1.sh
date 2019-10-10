#!/bin/bash


for l in {4..0}
do

i=1
while [ $i -le $l ]
do
echo -n " "
((i++))
done

m=$((5-$l))
j=1

while [ $j -le $m ]
do 
echo -n "#"
((j++))
done

echo " " 

done
