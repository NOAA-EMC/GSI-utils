#!/usr/bin/env python3
import matplotlib       # Matplotlib to make graphics
matplotlib.use('Agg')   # Need this to generate figs when not running an Xserver (e.g. via PBS/LSF)
from pickle import load
from datetime import datetime
import os.path
import argparse
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument('indir', help='directory to read in osense stat files')
parser.add_argument('outdir', help='directory to save plots')
args = parser.parse_args()

indir = args.indir
outdir = args.outdir

infilename = os.path.join(indir, 'osensestats_all.pkl')

print('loading  ' + infilename)
with open(infilename, 'rb') as infile:
    [exp, firstcycle, lastcycle, moist, dry, kin] = load(infile)

start = firstcycle.strftime("%Y-%m-%d")
end = lastcycle.strftime("%Y-%m-%d")

filename = os.path.join(outdir, exp + '_meantotal.png')
title = 'mean total impact per cycle (J/kg), ' + \
    exp + ' ' + start + ' to ' + end
ax = moist['mean total impact'].sort_values(ascending=False).plot.barh(
    xlabel='',
    ylabel='J/kg',
    title=title,
    figsize=(10, 6)
)
fig = ax.get_figure()
print('saving' + filename)
fig.savefig(filename, bbox_inches='tight')
fig.clear()

filename = os.path.join(outdir, exp + '_fractional.png')
title = 'fractional impact (%), ' + exp + ' ' + start + ' to ' + end
ax = moist['fractional impact'].sort_values().plot.barh(
    title=title,
    figsize=(10, 6)
)
fig = ax.get_figure()
print('saving' + filename)
fig.savefig(filename, bbox_inches='tight')
fig.clear()

filename = os.path.join(outdir, exp + '_obspercycle.png')
title = 'mean observations per cycle, ' + exp + ' ' + start + ' to ' + end
ax = moist['mean num obs'].sort_values().plot.barh(
    title=title,
    figsize=(10, 6)
)
fig = ax.get_figure()
print('saving' + filename)
fig.savefig(filename, bbox_inches='tight')
fig.clear()

filename = os.path.join(outdir, exp + '_impactperobs.png')
title = 'impact per observation (J/kg), ' + exp + ' ' + start + ' to ' + end
ax = moist['mean impact per ob'].sort_values(ascending=False).plot.barh(
    xlabel='',
    ylabel='J/kg',
    title=title,
    figsize=(10, 6)
)
fig = ax.get_figure()
print('saving' + filename)
fig.savefig(filename, bbox_inches='tight')
fig.clear()
