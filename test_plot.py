#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Specify encoding so strings can have special characters.
#

from __future__ import print_function
import sys
import os
from datetime import datetime, timedelta
import numpy as np



#not so common modules you might need to install 
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio
import chart_studio.plotly as charts

pio.renderers.default = "browser"
pio.templates.default = "plotly_white"

def exp_target_properties():
    print('Calling exp_target_properties()')
    
    """ Returns the dictionary of dictionaries for target properties. """
    target_props = {
        'names': {     # Translation table for long name to short name.
            'LH2': 1000,
            'LD2': 2000
        },
        'density': {     # Units: g/cm^2
            'LH2': 0.335,
            'LD2': 0.820
        },
         'color': {  # Plot color: r,g,b,a
             'LH2': 'rgba(0, 120, 150, 0.8)',
             'LD2': 'rgba(20, 80, 255, 0.8)'
        },
        'sums_color': {  # Plot color: r,g,b,a
            'LH2': 'rgba(255, 120, 150, 0.8)',
            'LD2': 'rgba(255, 80, 255, 0.8)'
        },
    }

    return target_props


def main(argv=None):
    import argparse


    
if __name__ == "__main__":
    sys.exit(main())
