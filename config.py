''' Configuration file for SVG to GCODE converter
    Date: 26 Oct 2016
    Author: Peter Scriven
'''


'''G-code emitted at the start of processing the SVG file'''
preamble = "G28\nG1 Z0.0\nM03 S255"

'''G-code emitted at the end of processing the SVG file'''
postamble = "G28 M03 S255"

'''G-code emitted before processing a SVG shape'''
shape_preamble = ""  #"G4 P0.2\n M03 S0"

'''G-code emitted after processing a SVG shape'''
shape_postamble = "G4 P0.2\nM03 S255 "

# A4 area:               210mm x 297mm
# Printer Cutting Area: ~178mm x ~344mm
# Testing Area:          150mm x 150mm  (for now)
'''Print bed width in mm'''
bed_max_x = 210

'''Print bed height in mm'''
bed_max_y = 234

''' Used to control the smoothness/sharpness of the curves.
    Smaller the value greater the sharpness. Make sure the
    value is greater than 0.1'''
smoothness = 0.1
