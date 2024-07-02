
import json
import PIL
from matplotlib import pyplot as plt
import numpy as np

import os
import glob

# Specify the directory containing the JSON files
directory = 'data/training_subset/'

# Use glob to list all JSON files in the directory
json_files = glob.glob(os.path.join(directory, '*.json'))

STANDARD_HEIGHT = 30
STANDARD_WIDTH = 30
IMG_DIMENSION = 128

def int_to_rgb(int):
        int_to_hex = {
        0: "#000000",  # black
        1: "#0074D9",  # blue
        2: "#FF4136",  # red
        3: "#2ECC40",  # green
        4: "#FFDC00",  # yellow
        5: "#AAAAAA",  # grey
        6: "#F012BE",  # fuschia
        7: "#FF851B",  # orange
        8: "#7FDBFF",  # teal
        9: "#870C25",  # brown
        -1: "#7200FF"  # purple (padding)
    }
        return list(PIL.ImageColor.getrgb(int_to_hex[int]))

def create_image_array(data):
        return np.array([[int_to_rgb(element) for element in row] for row in data], dtype=np.uint8)

# Iterate through the list of JSON files
for json_file in json_files:
    with open(json_file, 'r') as file:
        data = json.load(file)
        # # Process the JSON data
        # print(f"Processing file: {json_file}")
        # print(data)

    # with open('data/training/0a938d79.json') as json_file:
    #     data = json.load(json_file)

        train_data = data['train']

        for i in range(len(train_data)):
            example = train_data[i]
            data_array = np.array(example['input'])

    
            padded_array = np.pad(data_array, ((0, STANDARD_HEIGHT - data_array.shape[0]), (0, STANDARD_WIDTH - data_array.shape[1])), constant_values=-1)


            assert padded_array.shape == (30, 30), padded_array.shape


            


            padded_image_array = create_image_array(padded_array)



            # plt.imshow(padded_image_array, interpolation='nearest')


            padded_image = PIL.Image.fromarray(padded_image_array, 'RGB')


            padded_image = padded_image.resize((IMG_DIMENSION, IMG_DIMENSION), resample=PIL.Image.Resampling.NEAREST)


            # image = image.resize((2500, 1000), resample=Image.Resampling.NEAREST)

            json_filename = os.path.basename(json_file).strip('.json')

            padded_image.save('arc_images/' + json_filename + f'_input_{i}' + '.png')







