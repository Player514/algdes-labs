#!/bin/sh
PROGRAM_TO_RUN="Some.py"

OUT_FILE="results/${PROGRAM_TO_RUN}_out"
for FILE in data/*.txt; do
  printf "\n\nStarting ${FILE}\n"
  printf "${FILE}\t" >> ${OUT_FILE}
  python ${PROGRAM_TO_RUN} < "$FILE" >> ${OUT_FILE}
done
