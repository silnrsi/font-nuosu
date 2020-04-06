#!/usr/bin/python3
# -*- coding: utf-8 -*-

APPNAME = "NuosuSIL"
DESC_SHORT = "Unicode font for the Yi script"

getufoinfo('source/NuosuSIL-Regular.ufo')

fontfamily=APPNAME

designspace('source/' + fontfamily + '.designspace',
            target = "${DS:FILENAME_BASE}.ttf",
            pdf = fret(params="-r -oi")
)
