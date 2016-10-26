#!/usr/bin/python

import ephem

home = ephem.Observer()
home.horizon = '-12';
home.lat = '51.9786464'
home.lon = '-2.2415342'

print(home.previous_rising(ephem.Sun()))
