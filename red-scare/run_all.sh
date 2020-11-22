#!/bin/sh
PROGRAM_TO_RUN="some.py"

OUT_FILE="results/${PROGRAM_TO_RUN}_out"
printf "" > ${OUT_FILE}
for FILE in data/*.txt; do
  printf "\n\nStarting ${FILE}\n"
  printf "${FILE}\t" >> ${OUT_FILE}
  python ${PROGRAM_TO_RUN} < "$FILE" >> ${OUT_FILE}
  if [[ $? -ne 0 ]]; then
    printf "?\n" >> ${OUT_FILE}
  fi
done
