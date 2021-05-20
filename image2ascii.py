import cv2
from image_process import grayscale, resize_image

#index          0    1    2    3    4    5    6    7    8    9   10
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def pixels_to_ascii(image):
    '''
    Transform numpy.array image to an ascii string
    ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]
    11 types of stoke width in range 0 ~ 255
    image => numpy.array
    return type : string
    '''
    pixels = image.reshape(image.shape[0]*image.shape[1]) # return Tuples of RGB color code
    # join explain: use "" to link list or tuple of str object
    # ex: "-".join("a", "b", "c") # "a-b-c"
    # same as:
    # for pixel in pixels:
    #    characters += ASCII_CHARS[pixel//25]
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return characters

def image2ascii(path, new_width=100, writeFile=False):
    '''
    parameter:
    path: image_file path
    new_width : control width
    writeFile
    '''
    try:
        image = cv2.imread(path).astype(float)
    except:
        print(path, "is not valid path name to an image.\n")
        return

    new_image_data = pixels_to_ascii(grayscale(resize_image(image, new_width)))

    pixel_count = len(new_image_data) # total pixel count (len of str)
    
    # output function (here)
    # for i in range(0, pixel_count-new_width, new_width):
    #     print(new_image_data[i:i+new_width])
    ascii_image = "\n".join(\
                [new_image_data[index:(index+new_width)]\
                for index in range(0, pixel_count, new_width)])
    return ascii_image

    # write file
    if writeFile:
        # join with "\n", from 1D to 2D
        ascii_image = "\n".join(\
                [new_image_data[index:(index+new_width)]\
                for index in range(0, pixel_count, new_width)])

        # print(ascii_image)
        with open("ascii_image.txt", "w") as f:
            f.write(ascii_image)
