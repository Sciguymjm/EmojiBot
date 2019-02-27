import os
import random
from PIL import Image
from svgimgutils import SVGImgUtils

INKSCAPE_LOCATION = "\"C:\\Program Files\\Inkscape\\inkscape.exe\""


def process_parts():
    d = {}
    for folder in os.listdir('pngs'):
        d[folder] = []
        if os.path.isdir(os.path.join('pngs', folder)):
            files = os.listdir(os.path.join('pngs', folder))
            for f in files:
                fp = os.path.join('pngs', folder, f)
                d[folder].append(fp)
    return d

def convert_parts():
    d = {}
    for folder in os.listdir('parts'):
        if os.path.isdir(os.path.join('parts', folder)):
            files = os.listdir(os.path.join('parts', folder))
            for f in files:
                fp = os.path.join('parts', folder, f)
                # convert
                fp_converted = fp.replace('parts', 'pngs').replace('.svg', '.png')
                try:
                    os.makedirs(os.path.dirname(fp_converted))
                except:
                    pass
                os.system("{} {} -e {}".format(INKSCAPE_LOCATION, fp, fp_converted))
    return d

#convert_parts()
def generate():
    parts_list = process_parts()

    background = Image.open(random.choice(parts_list["bases"]))
    for part in ["eyes", "mouths", "eyebrows", "extras"]:
        if part == "bases":
            continue
        fn = random.choice(parts_list[part])
        foreground = Image.open(fn)
        background.paste(foreground, (0, 0), foreground)

    background.save("merged.png")


if __name__ == '__main__':
    generate()