import sys
import os
from PIL import Image

image_folder = sys.argv[1]
output_folder = sys.argv[2]

# if not os.path.exists(image_folder):
#     os.makedirs(image_folder)

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    print(clean_name)
    img.save(f'{output_folder}{clean_name}.png', 'png')
    print('All done!')


