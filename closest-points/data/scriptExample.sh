#!/bin/sh
rm close_pairs_our_solution.out.txt
touch close_pairs_our_solution.out.txt

for FILE in *-tsp.txt
do
	echo $FILE
    printf "../data/$FILE: " >> close_pairs_our_solution.out.txt
	base=${FILE%-in.txt}
    python3 ../src/solution.py < $FILE >> close_pairs_our_solution.out.txt
done

python3 unordered-diff.py close_pairs_our_solution.out.txt closest-pair-out.txt
