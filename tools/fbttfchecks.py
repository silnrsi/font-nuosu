#!/usr/bin/python3
'''Example for making project-specific changes to the standard pysilfont set of Font Bakery ttf checks.
It will start with all the checks normally run by pysilfont's ttfchecks profile then modify as described below'''
__url__ = 'http://github.com/silnrsi/pysilfont'
__copyright__ = 'Copyright (c) 2020 SIL International (http://www.sil.org)'
__license__ = 'Released under the MIT License (http://opensource.org/licenses/MIT)'
__author__ = 'David Raymond and Bobby de Vos'

from silfont.fbtests.ttfchecks import psfcheck_list, make_profile, check, PASS, FAIL

#
# General settings
#
psfvariable_font = False  # Set to True for variable fonts, so different checks will be run

#
# psfcheck_list is a dictionary of all standard Fontbakery checks with a dictionary for each check indicating
# pysilfont's standard processing of that check
#
# Specifically:
# - If the dictionary has "exclude" set to True, that check will be excluded from the profile
# - If change_status is set, the status values reported by psfrunfbchecks will be changed based on its values
# - If a change in status is temporary - eg just until something is fixed, use temp_change_status instead
#

# Checks to ignore
psfcheck_list['com.google.fonts/check/required_tables']['exclude'] = True
psfcheck_list['com.google.fonts/check/rupee']['exclude'] = True
psfcheck_list['com.google.fonts/check/gdef_spacing_marks']['exclude'] = True
psfcheck_list['com.google.fonts/check/gdef_mark_chars']['exclude'] = True
psfcheck_list['com.google.fonts/check/gdef_non_mark_chars']['exclude'] = True
psfcheck_list['com.google.fonts/check/gpos_kerning_info']['exclude'] = True
psfcheck_list['com.google.fonts/check/varfont/consistent_axes']['exclude'] = True
psfcheck_list['com.google.fonts/check/hinting_impact']['exclude'] = True
psfcheck_list['com.google.fonts/check/version_bump']['exclude'] = True
psfcheck_list['com.google.fonts/check/production_glyphs_similarity']['exclude'] = True
psfcheck_list['com.google.fonts/check/name/fullfontname']['exclude'] = True # check needs a rewrite
psfcheck_list['com.google.fonts/check/integer_ppem_if_hinted']['exclude'] = True
psfcheck_list['com.google.fonts/check/vertical_metrics_regressions']['exclude'] = True

#
#  Create the fontbakery profile
#
profile = make_profile(psfcheck_list, variable_font = psfvariable_font)
