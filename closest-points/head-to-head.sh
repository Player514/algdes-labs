#!/bin/sh
echo "1:"
printf "Divide-and-conquer:  "
start=$SECONDS
for FILE_NAME in data/*-tsp.txt; do
	python3 src/closestPoints.py < $FILE_NAME > /dev/null
done
duration=$(( SECONDS - start ))
echo $duration

printf "KD-tree:             "
start=$SECONDS
for FILE_NAME in data/*-tsp.txt; do
    python3 src/kd-solver.py < $FILE_NAME > /dev/null
done
duration=$(( SECONDS - start ))
echo $duration

echo "7:"
printf "Divide-and-conquer:  "
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

for FILE_NAME in data/*-tsp.txt; do
	python3 src/closestPoints.py < $FILE_NAME > /dev/null
done

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

printf "KD-tree:             "
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

for FILE_NAME in data/*-tsp.txt; do
    python3 src/kd-solver.py < $FILE_NAME > /dev/null
done

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

echo "20:"
printf "Divide-and-conquer:  "
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

for FILE_NAME in data/*-tsp.txt; do
	python3 src/closestPoints.py < $FILE_NAME > /dev/null
done

for FILE_NAME in data/*-tsp.txt; do
	python3 src/closestPoints.py < $FILE_NAME > /dev/null
done

for FILE_NAME in data/*-tsp.txt; do
	python3 src/closestPoints.py < $FILE_NAME > /dev/null
done

for FILE_NAME in data/*-tsp.txt; do
	python3 src/closestPoints.py < $FILE_NAME > /dev/null
done

for FILE_NAME in data/*-tsp.txt; do
	python3 src/closestPoints.py < $FILE_NAME > /dev/null
done

for FILE_NAME in data/*-tsp.txt; do
	python3 src/closestPoints.py < $FILE_NAME > /dev/null
done

for FILE_NAME in data/*-tsp.txt; do
	python3 src/closestPoints.py < $FILE_NAME > /dev/null
done

for FILE_NAME in data/*-tsp.txt; do
	python3 src/closestPoints.py < $FILE_NAME > /dev/null
done

for FILE_NAME in data/*-tsp.txt; do
	python3 src/closestPoints.py < $FILE_NAME > /dev/null
done

for FILE_NAME in data/*-tsp.txt; do
	python3 src/closestPoints.py < $FILE_NAME > /dev/null
done

for FILE_NAME in data/*-tsp.txt; do
	python3 src/closestPoints.py < $FILE_NAME > /dev/null
done

for FILE_NAME in data/*-tsp.txt; do
	python3 src/closestPoints.py < $FILE_NAME > /dev/null
done

for FILE_NAME in data/*-tsp.txt; do
	python3 src/closestPoints.py < $FILE_NAME > /dev/null
done

for FILE_NAME in data/*-tsp.txt; do
	python3 src/closestPoints.py < $FILE_NAME > /dev/null
done

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

printf "KD-tree:             "
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

for FILE_NAME in data/*-tsp.txt; do
    python3 src/kd-solver.py < $FILE_NAME > /dev/null
done

for FILE_NAME in data/*-tsp.txt; do
    python3 src/kd-solver.py < $FILE_NAME > /dev/null
done

for FILE_NAME in data/*-tsp.txt; do
    python3 src/kd-solver.py < $FILE_NAME > /dev/null
done

for FILE_NAME in data/*-tsp.txt; do
    python3 src/kd-solver.py < $FILE_NAME > /dev/null
done

for FILE_NAME in data/*-tsp.txt; do
    python3 src/kd-solver.py < $FILE_NAME > /dev/null
done

for FILE_NAME in data/*-tsp.txt; do
    python3 src/kd-solver.py < $FILE_NAME > /dev/null
done

for FILE_NAME in data/*-tsp.txt; do
    python3 src/kd-solver.py < $FILE_NAME > /dev/null
done

for FILE_NAME in data/*-tsp.txt; do
    python3 src/kd-solver.py < $FILE_NAME > /dev/null
done

for FILE_NAME in data/*-tsp.txt; do
    python3 src/kd-solver.py < $FILE_NAME > /dev/null
done

for FILE_NAME in data/*-tsp.txt; do
    python3 src/kd-solver.py < $FILE_NAME > /dev/null
done

for FILE_NAME in data/*-tsp.txt; do
    python3 src/kd-solver.py < $FILE_NAME > /dev/null
done

for FILE_NAME in data/*-tsp.txt; do
    python3 src/kd-solver.py < $FILE_NAME > /dev/null
done

for FILE_NAME in data/*-tsp.txt; do
    python3 src/kd-solver.py < $FILE_NAME > /dev/null
done

for FILE_NAME in data/*-tsp.txt; do
    python3 src/kd-solver.py < $FILE_NAME > /dev/null
done

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
