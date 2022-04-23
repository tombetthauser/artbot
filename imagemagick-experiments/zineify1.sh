# infile $1 outfile $2
IN=$1
OUT='out-'$1

# resize
convert $IN'[250x250]' $OUT

# grayscale & dither
convert $OUT -colorspace Gray -ordered-dither o8x8 $OUT

convert $OUT -channel RGB -negate $OUT

# draw replace topleft with color
convert $OUT -fill red -draw 'color 0,0 replace' $OUT

# invert
# convert $OUT -channel RGB -negate $OUT

# replace white with black
convert $OUT -fill black -opaque white $OUT

# open output image
open $OUT
