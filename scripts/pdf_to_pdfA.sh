#!/bin/bash

# Code originally from:
# https://brandonlucia.com/pdf-a-conversion.html

infile=${1}

outfile=${infile%%.*}_pdfA.pdf

gs -dPDFA -dBATCH -dNOPAUSE -sProcessColorModel=DeviceRGB -sDEVICE=pdfwrite -sPDFACompatibilityPolicy=3 -sOutputFile=${outfile} "${infile}"

echo "Done"
