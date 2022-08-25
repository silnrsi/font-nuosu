#!/usr/bin/python3
# this is a smith configuration file

APPNAME = "NuosuSIL"
DESC_SHORT = "Unicode font for the Yi script"

getufoinfo('source/NuosuSIL-Regular.ufo')
# BUILDLABEL = 'beta1'

# Set up the FTML tests
ftmlTest('tools/ftml-smith.xsl')

fontfamily=APPNAME

designspace('source/' + fontfamily + '.designspace',
            target = "${DS:FILENAME_BASE}.ttf",
            version = VERSION,
            woff = woff('web/${DS:FILENAME_BASE}',
                metadata = '../source/${DS:FAMILYNAME_NOSPC}-WOFF-metadata.xml'),
            pdf = fret(params="-r -oi")
)
