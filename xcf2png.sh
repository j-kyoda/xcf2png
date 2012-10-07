#!/bin/sh
# -*- coding: utf-8 -*-

cmd_gimp=gimp-2.8
lib_path=.

ext=.png
flat=False

function export_images {
    xcf_path=$1
    img_path=$2

    init="import sys; sys.path.insert(0, \"${lib_path}\"); import xcf2img; "
    cmd="xcf2img.run(\"${xcf_path}\", \"${img_path}\", \"${ext}\", ${flat})"
    echo ${cmd}
    ${cmd_gimp} -idf --batch-interpreter python-fu-eval -b "${init}${cmd}"
}

if [ $# -ne 2 ]
then
    echo "usage: $0 XCF_DIR PNG_DIR"
    exit 1
fi
export_images $1 $2
