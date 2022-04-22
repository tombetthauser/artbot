convert in.jpg -colorspace GRAY -resize 500 png:out.png
convert out.png -ordered-dither h8x8o png:out.png
convert out.png -morphology smooth Disk:2.5 png:out.png
convert out.png -normalize png:-
