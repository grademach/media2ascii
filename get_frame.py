from PIL import Image

brightnessLevels = " .-+*wGHM#&%@"
# brightnessLevels = " .-"
# terminalResolution = (209, 52)
terminalResolution = (50, 40)

def image_to_ascii(path: str, resolution: tuple=terminalResolution):

    img = Image.open(path)
    img = img.convert("L").resize(resolution)
    pixels = img.load()
    WIDTH = img.width
    HEIGHT = img.height
    pixelsOut = []

    for y in range(HEIGHT):
        for x in range(WIDTH):
            px = pixels[x, y]
            brLevel = round((len(brightnessLevels)-1) * (px / 255))
            character = brightnessLevels[brLevel]
            pixelsOut.append(character)

    for i in range(HEIGHT):
        pixelsOut[WIDTH*i] = "\n"

    img.close()
    return "".join(pixelsOut)