#!/bin/bash

# Code originally from:
# http://stackoverflow.com/questions/11828528/display-first-page-of-pdf-as-image

infile=${1}

outfile=${infile%%.*}_thumb.jpg

# gs -q -dFirstPage=1 -dLastPage=1 -o $(basename "${infile}")_p%04d.jpeg -sDEVICE=jpeg "${infile}"

# To get thumbnail JPEGs with a width 200 pixel use the following command:
# gs -q -dFirstPage=1 -dLastPage=1 -o name_200px_p%04d.jpg -sDEVICE=jpeg -dPDFFitPage -g200x400 "${infile}"

# To get higher quality JPEGs (but also bigger-in-size ones) with a 
# resolution of 300 dpi use the following command:
# gs -q -dFirstPage=1 -dLastPage=1 -o name_300dpi_p%04d.jpg -sDEVICE=jpeg -dJPEGQ=100 -r300 "${infile}"

gs -q -dFirstPage=1 -dLastPage=1 -o ${outfile} -sDEVICE=jpeg -dJPEGQ=100 -r100 "${infile}"

echo "Done"
