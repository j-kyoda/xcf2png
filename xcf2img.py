#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
from glob import glob

import gimpfu

def convert(pdb, filename, out_filename, flat):
    img = pdb.gimp_file_load(filename, filename)

    if flat:
        img.flatten()
        layer = img.layers[0]
    else:
        layer = pdb.gimp_image_merge_visible_layers(img, gimpfu.CLIP_TO_IMAGE)

    pdb.gimp_file_save(img, layer, out_filename, out_filename)
    pdb.gimp_image_delete(img)

def run(xcfdir=".", imgdir=".", ext=".png", flat=False):
    pdb = gimpfu.pdb
    pathname = os.path.join(xcfdir, "*.xcf")
    for xcf_file in glob(pathname):
        base_name = os.path.basename(xcf_file).rsplit(".",1)[0]
        img_file = os.path.join(imgdir, base_name) + ext

        convert(pdb, xcf_file, img_file, flat)
    pdb.gimp_quit(1)

