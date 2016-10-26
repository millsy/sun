#!/usr/bin/python

import ephem
import sys, getopt
from datetime import datetime

class MySun():
	def __init__(self, argv):
   		self.home = ephem.Observer()
	   	self.home.lat = '51.9786464'
	   	self.home.lon = '-2.2415342'
	   	self.home.horizon = '-6'
   		try:
		      	opts, args = getopt.getopt(argv,"ha:o:z:")
	   	except getopt.GetoptError:
		      	print 'sunrise.py -a lat -o long -z horizon'
		      	print 'Example usage: sunrise.py -a 51.9786464 -o -2.2415342 -z 6'
		      	sys.exit(2)
	   	for opt, arg in opts:
		      	if opt == '-h':
         			print 'sunrise.py -a lat -o long -z horizon'
		         	print 'Example usage: sunrise.py -a 51.9786464 -o -2.2415342 -z -6'
         			sys.exit()
		      	elif opt in ("-a"):
         			self.home.lat = arg
		      	elif opt in ("-o"):
		         	self.home.lon = arg
		      	elif opt in ("-z"):
		         	self.home.horizon = arg

	def lastrise(self) :
		return self.home.previous_rising(ephem.Sun())
	def nextset(self) :
		return self.home.next_setting(ephem.Sun())

if __name__ == "__main__":
	sun = MySun(sys.argv[1:])
	print(sun.lastrise())
	print(sun.nextset())
