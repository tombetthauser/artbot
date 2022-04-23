convert in.jpg -colorspace GRAY -resize 500 png:out.png
convert out.png -ordered-dither h8x8o png:out.png
convert out.png -morphology smooth Disk:2.5 png:out.png
convert out.png -normalize png:-


convert in.png -colorspace Gray -ordered-dither o8x8 out.png

convert in.png'[500x500]' out.png

convert in.png -channel RGB -negate out.png

convert in.jpg -fuzz XX% -fill red -opaque black out.jpg

convert in.png -fill red -draw 'color 0,400 replace' out.png

magick in.png -alpha off -auto-threshold otsu out.png

convert in.png -colorspace gray out.png

convert in.png -alpha set -channel RGB -fill red -opaque black out.gif

# edge trace
convert A_image.gif -colorspace gray -edge 1 -fuzz 1% -trim +repage A_image_edge.gif
