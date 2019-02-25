import os
import random

import svg_stack as ss






def process_parts():
    d = {}
    for folder in os.listdir('parts'):
        d[folder] = []
        if os.path.isdir(os.path.join('parts', folder)):
            files = os.listdir(os.path.join('parts', folder))
            for f in files:
                d[folder].append(os.path.join('parts', folder, f))
    return d


parts_list = process_parts()

from svgimgutils import SVGImgUtils

# Create SVG Image Utils for each SVG image
base_template = SVGImgUtils.fromfile(random.choice(parts_list['bases']))



for part in parts_list:
    if part == 'bases':
        continue # we already have a base
    base_template.append(SVGImgUtils.fromfile(random.choice(parts_list[part])))

# Save new merged SVG image
base_template.save('merged.svg')







doc = ss.Document()

layout1 = ss.VBoxLayout()

doc.setLayout(layout1)

doc.save('qt_api_test.svg')
