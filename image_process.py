import cv2
import numpy as np

# Bi-Linear interpolation
def bl_interpolate(img, new_width=100, new_height=100):
    '''
    Bilinear image transform
    parameter: 
        img        -> numpy.array(float)
        new_width  -> int
        new_height -> int
    '''
    H, W, C = img.shape # height, width, color

    aH = new_height # new_height
    aW = new_width # new_width

    # get position of resized image
    y = np.arange(aH).repeat(aW).reshape(aH, -1)
    x = np.tile(np.arange(aW), (aH, 1))

    # get position of original position
    y = y / (aH / H)
    x = x / (aW / W)

    ix = np.floor(x).astype(int)
    iy = np.floor(y).astype(int)

    ix = np.minimum(ix, W-2) # boundry side will be out of bound, so (W -1) - 1 for case
    iy = np.minimum(iy, H-2)

    # get distance 
    dx = x - ix
    dy = y - iy

    # expand to RGB mode(copy as the same value)
    # ex: (255) -> (255, 255, 255), ...
    dx = np.repeat(np.expand_dims(dx, axis=-1), 3, axis=-1)
    dy = np.repeat(np.expand_dims(dy, axis=-1), 3, axis=-1)

    # interpolation
    # bileaner core function
    out = (1-dx) * (1-dy) * img[iy, ix] + dx * (1 - dy) * img[iy, ix+1] + (1 - dx) * dy * img[iy+1, ix] + dx * dy * img[iy+1, ix+1]

    # constrain the numbers get inside of range (0~255)
    out = np.clip(out, 0, 255)

    # 8 bits unsign interger(0~255)
    out = out.astype(np.uint8)

    return out

def resize_image(image, new_width=100):
    '''
    image => numpy.array
    new_width => int
    return type : numpy.array
    '''
    width, height = image.shape[:2]
    ratio = height / width / 1.8 # scale the same ratio of width and height
    new_height = int(new_width * ratio)
    resized_image = bl_interpolate(image, new_width, new_height)  # What we need to do research

    return resized_image

def grayscale(img):
    '''
    Gray Scale
    parameter:
        img->numpy.array(unit8)
    Average R G B
    '''
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            r = img[i][j][0]
            g = img[i][j][1]
            b = img[i][j][2]
            gray = int(r/3+g/3+b/3)
            img[i][j][0] = img[i][j][1] = img[i][j][2] = gray
    return img[:,:,0]
    
# # Read image
# img = cv2.imread("image/mountain.jpg").astype(float)
# # Bilinear interpolation
# out = bl_interpolate(img, new_width=400, new_height=320)
# out = grayscale(out)
# print(out.shape)

# # Save result
# cv2.imshow("result", out)
# cv2.waitKey(0)
# cv2.imwrite("out.jpg", out)