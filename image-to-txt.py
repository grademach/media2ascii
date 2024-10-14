from get_frame import image_to_ascii

img = "perro.jpg"

with open("img.txt", "w") as f:
    f.write(image_to_ascii(img))