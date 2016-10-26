#!/usr/bin/python

import ephem
import sys, getopt


def main(argv):
   home = ephem.Observer()
   lat = '51.9786464'
   lon = '-2.2415342'
   horizon = '-6'
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
         lat = arg
      elif opt in ("-o"):
         lon = arg
      elif opt in ("-z"):
         horizon = arg
   home.lon = lon
   home.lat = lat
   home.horizon = horizon
   print(home.previous_rising(ephem.Sun()))

if __name__ == "__main__":
   main(sys.argv[1:])
