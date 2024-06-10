import sys
from PIL import Image, ImageOps

image_formats = ('.jpg', '.jpeg', '.png')
if len(sys.argv) > 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) < 3:
    sys.exit("Too many command-line arguments")
else:
    if sys.argv[1].endswith(image_formats) and sys.argv[2].endswith(image_formats) :
        if sys.argv[1].split('.')[1] == sys.argv[2].split('.')[1]:
             file1 = sys.argv[1]
             file2 = sys.argv[2]
        else:
            sys.exit("Input and output have different extensions")
    else:
        sys.exit("Invalid input")

try:
    shirt = Image.open("shirt.png")
    with Image.open(file1) as input:
        input_cropped = ImageOps.fit(input, shirt.size)
        input_cropped.paste(shirt, mask = shirt)
        input_cropped.save(file2)
except FileNotFoundError:
    sys.exit(f"Input does not exist")
