# infile $1 outfile $2
IN=$1
OUT='out-'${1%.*}.png

# resize
convert $IN'[1350x1350]' $OUT

# [brightness]x[contrast]
convert -brightness-contrast -20x50 $OUT $OUT

# grayscale & dither
# convert $OUT -colorspace Gray -ordered-dither o8x8 $OUT

# trace edges
# convert $OUT -colorspace Gray -edge 1 -fuzz 1% -trim +repage $OUT
convert $OUT -edge 1 -fuzz 1% +repage $OUT

# dither color
# convert $OUT -ordered-dither o8x8 $OUT

# invert
convert $OUT -channel RGB -negate $OUT

# draw replace topleft with color
# convert $OUT -fill red -draw 'color 0,0 replace' $OUT

# replace white with black
# convert $OUT -fill black -opaque white $OUT

# open output image
open $OUT
