from news_project.utils.main_utils import read_yaml_file
from news_project.constants import *
import pandas as pd
import os
# from pandas import DataFrame

# target_encodings = read_yaml_file(SCHEMA_FILE_PATH)
# print(target_encodings)
# # print(type(data['target_encoding'][0]))

# series = pd.Series(['business', 'sport'])
# # print(series)
# # print(type(series))

# print(series.map(target_encodings))
# # print(data.to_dict())
# yaml_file = read_yaml_file(os.path.join('params.yaml'))
# print(yaml_file['RANDOM_STATE'])

from PIL import Image, ImageDraw, ImageFont

# Open the text file
with open('modelsummary.txt', 'r') as f:
    text = f.read()

# Create an image
img = Image.new('RGB', (600, 400), (255, 255, 255))  # Adjust size as needed
draw = ImageDraw.Draw(img)

# Choose a font
font = ImageFont.truetype("arial.ttf", 20)  # Adjust font and size

# Draw the text on the image
draw.text((10, 10), text, font=font, fill=(0, 0, 0))

# Save the image
img.save('text_as_image.png')