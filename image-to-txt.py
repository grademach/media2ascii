from get_frame import image_to_ascii

img = "./perro.jpg"
resolution = (100, 80)

with open("image.txt", "w") as f:
    f.write(image_to_ascii(img, resolution))