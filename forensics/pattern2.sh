#!/bin/bash
a=8
b=1
for i in {1..7}
do
z=1
while [ $z -le $a ]
do
echo -n " "
((z++))
done

x=1
while [ $x -le $b ]
do
echo -n "#"
((x++))
done

echo

((a--))
b=$(($b+2))
done
