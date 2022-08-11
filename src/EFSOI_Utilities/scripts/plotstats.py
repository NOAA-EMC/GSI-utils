#!/usr/bin/env python3
from pickle import load
from datetime import datetime
import os.path
import argparse
import pandas as pd
import osense

parser = argparse.ArgumentParser()
parser.add_argument('indir', help='directory to read in osense stat files')
parser.add_argument('outdir', help='directory to save plots')
args = parser.parse_args()

indir = args.indir
outdir = args.outdir


norms = ['osense_kin', 'osense_dry', 'osense_moist']

infilename = os.path.join(indir, 'osensestats_all.pkl')

print('loading  ' + infilename)
with open(infilename, 'rb') as infile:
    [firstcycle, lastcycle,moist, dry, kin] = load(infile)


filename= os.path.join(outdir, 'meantotal.png')
title='mean total impact per cycle (J/kg)'
ax=moist['mean total impact'].sort_values(ascending=False).plot.barh(
    xlabel='',
    ylabel='J/kg',
    title=title,
    figsize=(10, 6)
    )
fig=ax.get_figure()
fig.savefig(filename,bbox_inches='tight')
fig.clear()

filename= os.path.join(outdir, 'fractional.png')
title='fractional impact (%)'
ax=moist['fractional impact'].sort_values().plot.barh(
    title=title,
    figsize=(10, 6)
    )
fig=ax.get_figure()
fig.savefig(filename,bbox_inches='tight')
fig.clear()

filename= os.path.join(outdir, 'obspercycle.png')
title='mean observations per cycle' 
ax=moist['mean num obs'].sort_values().plot.barh(
    title=title,
    figsize=(10, 6)
    )
fig=ax.get_figure()
fig.savefig(filename,bbox_inches='tight')
fig.clear()

filename= os.path.join(outdir, 'impactperobs.png')
title='impact per observation (J/kg)' 
ax=moist['mean impact per ob'].sort_values(ascending=False).plot.barh(
    xlabel='',
    ylabel='J/kg',
    title=title,
    figsize=(10, 6)
    )
fig=ax.get_figure()
fig.savefig(filename,bbox_inches='tight')
fig.clear()

