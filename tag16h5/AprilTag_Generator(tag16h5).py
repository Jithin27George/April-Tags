import numpy as np
from PIL import Image

def mask(tag_id):
    tag_size = 6  # The total size of the tag (6x6 grid)
    cell_size = 20  # Each cell is scaled up by this factor

    # Creating a 6x6 array with 255 (white) values
    white_blanks = np.ones((6, 6)) * 255

    code=codeblock[tag_id]
    # Converting the list to a 4x4 NumPy array
    array_4x4 = np.array(code).reshape(4, 4)

    # Setting the border (first and last row/column) to 0 (black)
    white_blanks[0, :] = 0
    white_blanks[-1, :] = 0
    white_blanks[:, 0] = 0
    white_blanks[:, -1] = 0

    # Filling in the middle 4x4 section based on the values from array_4x4
    for i in range(4):  # Loop over rows
        for n in range(4):  # Loop over columns
            if array_4x4[i, n] == 0:
                white_blanks[i + 1, n + 1] = 0  # Set corresponding element to 0

    # Create the image from the array and scale it up
    img = Image.fromarray(white_blanks).convert('L')  # Ensure it's grayscale
    img = img.resize((tag_size * cell_size, tag_size * cell_size), resample=Image.NEAREST)

    return array_4x4, white_blanks, img

codeblock ={
    0: [0,0,1,0,0,0,1,1,0,0,0,1,1,0,1,1],
    1: [0,0,1,0,1,1,1,0,1,0,1,0,0,1,0,1],
    2: [0,0,1,1,0,1,0,0,0,1,1,0,1,0,1,0],
    3: [0,1,0,0,0,1,0,1,1,0,1,1,1,0,0,1],
    4: [0,1,1,1,1,0,0,1,1,0,1,0,0,1,1,0],
    5: [0,1,1,1,1,1,1,1,0,1,1,0,1,0,1,1],
    6: [1,0,1,1,0,0,1,1,0,1,0,1,1,0,0,0],
    7: [1,1,1,0,0,1,1,1,0,1,0,0,0,1,0,1],
    8: [1,1,1,1,1,1,1,0,0,1,0,1,1,0,0,1],
    9: [0,0,0,1,0,1,0,1,0,1,1,0,1,1,0,1],
    10: [0,0,1,1,1,0,0,0,0,0,0,0,1,0,1,1],
    11: [1,1,1,1,0,0,0,0,1,0,1,0,1,0,1,1],
    12: [0,0,0,0,1,1,0,1,1,0,0,0,0,1,0,0],
    13: [0,1,0,0,0,1,1,1,0,0,1,1,0,1,1,0],
    14: [1,0,0,0,1,1,0,0,0,1,1,1,0,0,1,0],
    15: [1,0,1,0,1,1,1,1,0,0,0,1,0,0,0,0],
    16: [0,0,0,0,1,0,0,1,0,0,1,1,1,1,0,0],
    17: [1,0,0,1,0,0,1,1,1,0,1,1,0,1,0,0],
    18: [1,0,1,0,0,1,0,1,0,0,0,0,0,0,1,1],
    19: [0,1,0,0,0,1,1,0,1,0,0,0,1,1,1,1],
    20: [1,1,1,0,0,0,0,1,0,0,1,1,0,1,1,1],
    21: [0,1,0,1,0,1,1,1,1,0,0,1,0,1,0,1],
    22: [1,1,0,1,1,1,1,1,0,1,0,0,0,0,1,0],
    23: [0,0,0,1,1,1,0,0,0,0,0,1,1,1,0,1],
    24: [1,1,1,0,1,0,0,1,1,1,0,1,1,1,0,0],
    25: [0,1,1,1,0,0,1,1,1,0,1,0,1,1,0,1],
    26: [1,0,1,0,1,1,0,1,0,1,0,1,1,1,1,1],
    27: [1,1,0,1,0,1,0,1,0,0,1,1,0,0,0,0],
    28: [0,0,0,0,0,1,1,1,1,1,0,0,1,0,1,0],
    29: [1,0,1,0,1,1,1,1,0,0,1,0,1,1,1,0],
}

if __name__ == "__main__":
    
    for tag_id in range (0,29):
             
        # Call the mask function to get the arrays and image
        array_4x4, white_blanks, img = mask(tag_id)
        
        # Printing the 4x4 array
        print("4x4 Array from List:")
        print(array_4x4)
        
        print("\nWhite Blanks Array (after applying the mask):")
        print(white_blanks)
        
        # Save the image to a file
        img.save(f'apriltag16h5_{tag_id}.png')
        print(f"AprilTag {tag_id} saved as 'apriltag16h5_{tag_id}.png'.")
