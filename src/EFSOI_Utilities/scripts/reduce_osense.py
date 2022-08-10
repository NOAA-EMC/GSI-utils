#!/usr/bin/env python3
from pickle import dump
from datetime import datetime
import os.path
import argparse
import sys
import pandas as pd
import osense

parser = argparse.ArgumentParser()
parser.add_argument(
    'firstcycle',
    help='first cycle to process, format YYYY-MM-DD-HH',
    type=lambda s: datetime.strptime(s, '%Y-%m-%d-%H'))
parser.add_argument(
    'lastcycle',
    help='last cycle to process, format YYYY-MM-DD-HH',
    type=lambda s: datetime.strptime(s, '%Y-%m-%d-%H'))
parser.add_argument('indir', help='directory to read in osense files')
parser.add_argument('outdir', help='directory to save output')
args = parser.parse_args()

firstcycle = args.firstcycle
lastcycle = args.lastcycle
indir = args.indir
outdir = args.outdir

cycletimes = ['00', '06', '12', '18']

if lastcycle < firstcycle:
    print('lastcycle', lastcycle, 'comes before firstcycle',
          firstcycle, ', you probably don\'t want that')
    sys.exit(1)

if firstcycle.strftime("%H") not in cycletimes:
    print('firstcycle', firstcycle,
          'needs to have an hour that is one of', cycletimes)
    sys.exit(1)

if lastcycle.strftime("%H") not in cycletimes:
    print('lastcycle', lastcycle, 'needs to have an hour that is one of', cycletimes)
    sys.exit(1)

if not os.path.isdir(indir):
    print('indir', indir, 'is not a directory')
    sys.exit(1)

if not os.path.isdir(outdir):
    print('outdir', outdir, 'is not a directory')
    sys.exit(1)


print('running from', firstcycle, 'to', lastcycle)

# time between cycles
cycles = pd.date_range(firstcycle, lastcycle, freq='6H')


for cycle in cycles:

    CDATE = cycle.strftime("%Y%m%d%H")
    PDY = cycle.strftime("%Y%m%d")
    cyc = cycle.strftime("%H")

    filename = os.path.join(indir, 'osense_' + CDATE + '_final.dat')

    if not os.path.isfile(filename):
        print('skipping ' + filename)
        continue

    (convdata, satdata, idate) = osense.read_osense(filename)

    osensedata = osense.consolidate(convdata, satdata)

    outfilename = os.path.join(outdir, 'osense_' + CDATE + '.pkl')
    print("saving file ", outfilename)
    with open(outfilename, 'wb') as outfile:
        dump([idate, osensedata], outfile)
