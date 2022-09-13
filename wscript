#!/usr/bin/python3
# this is a smith configuration file

# set the default output folders
DOCDIR = ['documentation', 'web']

# set the font name, version, licensing and description
APPNAME = 'NuosuSIL'
FAMILY = APPNAME
getufoinfo('source/NuosuSIL-Regular.ufo')

# Set up the FTML tests
ftmlTest('tools/ftml-smith.xsl')

designspace('source/' + FAMILY + '.designspace',
            target = "${DS:FILENAME_BASE}.ttf",
            version = VERSION,
            woff = woff('web/${DS:FILENAME_BASE}',
                metadata = '../source/${DS:FAMILYNAME_NOSPC}-WOFF-metadata.xml'),
            pdf = fret(params="-oi")
)
