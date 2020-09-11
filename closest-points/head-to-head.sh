#!/bin/sh
printf "KD-tree:             "
start=$SECONDS
for FILE_NAME in data/*-tsp.txt; do
	python3 src/closestPoints.py < $FILE_NAME > /dev/null
done

for FILE_NAME in data/*-tsp.txt; do
	python3 src/closestPoints.py < $FILE_NAME > /dev/null
done

for FILE_NAME in data/*-tsp.txt; do
	python3 src/closestPoints.py < $FILE_NAME > /dev/null
done
duration=$(( SECONDS - start ))
echo $duration

printf "Divide-and-conquer:  "
start=$SECONDS
for FILE_NAME in data/*-tsp.txt; do
    python3 src/kd-solver.py < $FILE_NAME > /dev/null
done

for FILE_NAME in data/*-tsp.txt; do
    python3 src/kd-solver.py < $FILE_NAME > /dev/null
done

for FILE_NAME in data/*-tsp.txt; do
    python3 src/kd-solver.py < $FILE_NAME > /dev/null
done
duration=$(( SECONDS - start ))
echo $duration

# printf "Divide-and-conquer 2:"
# start=$SECONDS
# for FILE_NAME in data/*-tsp.txt; do
#     python3 src/Andreascp.py < $FILE_NAME > /dev/null
# done
# duration=$(( SECONDS - start ))
# echo $duration