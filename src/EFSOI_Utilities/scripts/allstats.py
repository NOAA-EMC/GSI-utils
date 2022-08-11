#!/usr/bin/env python3
from pickle import dump, load
from datetime import datetime
import os.path
import argparse
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
parser.add_argument(
    'indir', help='directory to read and write osense stat files')
args = parser.parse_args()

firstcycle = args.firstcycle
lastcycle = args.lastcycle
indir = args.indir


norms = ['osense_kin', 'osense_dry', 'osense_moist']

# there's a better way to do this, maybe with xarrays
moist_count = pd.DataFrame()
moist_mean = pd.DataFrame()
moist_sum = pd.DataFrame()
dry_count = pd.DataFrame()
dry_mean = pd.DataFrame()
dry_sum = pd.DataFrame()
kin_count = pd.DataFrame()
kin_mean = pd.DataFrame()
kin_sum = pd.DataFrame()

print('running from', firstcycle, 'to', lastcycle)

cycles = osense.make_cycles(firstcycle, lastcycle)

for cycle in cycles:

    CDATE = cycle.strftime("%Y%m%d%H")

    infilename = os.path.join(indir, 'osensestats_' + CDATE + '.pkl')

    if not os.path.isfile(infilename):
        print(infilename + ' doesn\'t exist, skipping')
        continue

    print('loading  ' + infilename)
    with open(infilename, 'rb') as infile:
        [exp, cdate, meanimpacts, sumimpacts, obcounts] = load(infile)

    moist_count = pd.concat([moist_count, obcounts['osense_moist']], axis=1)
    moist_mean = pd.concat([moist_mean, meanimpacts['osense_moist']], axis=1)
    moist_sum = pd.concat([moist_sum, sumimpacts['osense_moist']], axis=1)
    dry_count = pd.concat([dry_count, obcounts['osense_dry']], axis=1)
    dry_mean = pd.concat([dry_mean, meanimpacts['osense_dry']], axis=1)
    dry_sum = pd.concat([dry_sum, sumimpacts['osense_dry']], axis=1)
    kin_count = pd.concat([kin_count, obcounts['osense_kin']], axis=1)
    kin_mean = pd.concat([kin_mean, meanimpacts['osense_kin']], axis=1)
    kin_sum = pd.concat([kin_sum, sumimpacts['osense_kin']], axis=1)

columns = ['mean total impact', 'fractional impact',
           'mean num obs', 'mean impact per ob']
moist = pd.DataFrame(columns=columns)
dry = pd.DataFrame(columns=columns)
kin = pd.DataFrame(columns=columns)


# The abs operators are in here so that all of the fractional impacts are
# positive whether the mean impacts are negative or positive
moist['mean total impact'] = moist_sum.mean(axis=1)
moist_impact_sum = abs(moist['mean total impact']).sum()
moist['fractional impact'] = abs(
    moist['mean total impact'])/moist_impact_sum * 100
moist['mean num obs'] = moist_count.mean(axis=1)
moist['mean impact per ob'] = moist['mean total impact']/moist['mean num obs']

dry['mean total impact'] = dry_sum.mean(axis=1)
dry_impact_sum = abs(dry['mean total impact']).sum()
dry['fractional impact'] = abs(dry['mean total impact'])/dry_impact_sum * 100
dry['mean num obs'] = dry_count.mean(axis=1)
dry['mean impact per ob'] = dry['mean total impact']/dry['mean num obs']

kin['mean total impact'] = kin_sum.mean(axis=1)
kin_impact_sum = abs(kin['mean total impact']).sum()
kin['fractional impact'] = abs(kin['mean total impact'])/kin_impact_sum * 100
kin['mean num obs'] = kin_count.mean(axis=1)
kin['mean impact per ob'] = kin['mean total impact']/kin['mean num obs']

outfilename = os.path.join(indir, 'osensestats_all.pkl')
print("saving file ", outfilename)
with open(outfilename, 'wb') as outfile:
    dump([exp, firstcycle, lastcycle, moist, dry, kin], outfile)
