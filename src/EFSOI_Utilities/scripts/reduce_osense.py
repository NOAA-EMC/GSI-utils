#!/usr/bin/env python3
from pickle import dump
from datetime import datetime
import os.path
import argparse
#import sys
#import pandas as pd
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
parser.add_argument('outdir', help='directory to save reduced osense files')
args = parser.parse_args()

firstcycle = args.firstcycle
lastcycle = args.lastcycle
indir = args.indir
outdir = args.outdir

print('running from', firstcycle, 'to', lastcycle)

cycles = osense.make_cycles(firstcycle, lastcycle)

for cycle in cycles:

    CDATE = cycle.strftime("%Y%m%d%H")

    filename = os.path.join(indir, 'osense_' + CDATE + '_final.dat')

    if not os.path.isfile(filename):
        print(filename + ' doesn\'t exist, skipping')
        continue

    (convdata, satdata, idate) = osense.read_osense(filename)

    osensedata = osense.consolidate(convdata, satdata)

    outfilename = os.path.join(outdir, 'osense_' + CDATE + '.pkl')
    print("saving file ", outfilename)
    with open(outfilename, 'wb') as outfile:
        dump([idate, osensedata], outfile)
