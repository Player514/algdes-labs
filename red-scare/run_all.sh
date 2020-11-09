#!/bin/sh
for FILE in data/*.txt; do
  echo "$FILE"
  python Some.py < "$FILE"
done
