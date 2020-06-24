#!/bin/bash
for file in *.txt; do
  cat $file >> combined.out
  printf '\n\n=========\n\n' >> combined.out
done
