#!/usr/bin/env python3
from pickle import dump, load
from datetime import datetime
import os.path
import argparse
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
parser.add_argument('indir', help='directory to read in reduced osense files')
parser.add_argument('outdir', help='directory to save stat files')
args = parser.parse_args()

firstcycle = args.firstcycle
lastcycle = args.lastcycle
indir = args.indir
outdir = args.outdir

grouping = 'source'
#grouping = 'detailed_source'
norms = ['osense_kin', 'osense_dry', 'osense_moist']

cycles = osense.make_cycles(firstcycle, lastcycle)

print('running from', firstcycle, 'to', lastcycle)

for cycle in cycles:

    CDATE = cycle.strftime("%Y%m%d%H")

    infilename = os.path.join(indir, 'osense_' + CDATE + '.pkl')

    if not os.path.isfile(infilename):
        print(infilename + ' doesn\'t exist, skipping')
        continue

    print('loading  ' + infilename)
    with open(infilename, 'rb') as infile:
        [exp, cdate, osensedata] = load(infile)

    columns = [grouping] + norms
    meanimpacts = osensedata[columns].groupby(grouping).mean()
    sumimpacts = osensedata[columns].groupby(grouping).sum()
    obcounts = osensedata[columns].groupby(grouping).count()

    outfilename = os.path.join(outdir, 'osensestats_' + CDATE + '.pkl')
    print("saving file ", outfilename)
    with open(outfilename, 'wb') as outfile:
        dump([exp, cdate, meanimpacts, sumimpacts, obcounts], outfile)
