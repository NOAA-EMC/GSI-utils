#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 14:23:41 2022

@author: mossland
"""
# Default imports
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import pandas as pd
import pickle
import datetime
import os.path
import matplotlib.colors as colors
import matplotlib.cm as cmx

CDATE = '2021121000'
exp='rodeo'
exp='baily'

#datadir='/work2/noaa/stmp/aeichman/comrot/' + exp + '/osense/'
#datadir='/work/noaa/stmp/aeichman/comrot/' + exp + '/osense/'
rootdir = '/Users/mossland/Desktop/work/EFSOI/' + exp 
indir = rootdir + '/consolidated/'

filename = indir + 'osense_' + CDATE + '.pkl'
infile = open( filename ,'rb')
[ idata, osensedata ] = pickle.load(infile)
infile.close()


# drop message='NA'/message02='Empty'
# data not dumped/not used
indices=osensedata[osensedata['assimilated']==0].index
osensedata.drop(indices,inplace = True)

source = 'Radiosonde'
source = 'AMSUA'
source = 'Ocean_Surface'
source = 'Aircraft'

for source in osensedata.source.unique():
#for source in ['Radiosonde','AMSUA','Ocean_Surface','Aircraft']:
    
    
    source = str( source )
    print('doing ' + source )

    lon = osensedata.loc[osensedata['source'] == source ]['lon']
    
    lon = osensedata.loc[osensedata['source'] == source ]['lon']
    lat = osensedata.loc[osensedata['source'] == source ]['lat']
    vals = osensedata.loc[osensedata['source'] == source ]['osense_moist']
 
#    vmin = vals.min()
#    vmax = vals.max()
#    maxval = max(abs(vmin),vmax)
#    vmin=-maxval/10
#    vmax=maxval/10
    valmean = vals.mean()
    valsstd = vals.std()
#    vmin = valmean - valsstd
#    vmax = valmean + valsstd    
    vmin = -valsstd
    vmax = valsstd 

    
    print('vmin, vmax: ' , vmin,vmax)
    rnbw = cm = plt.get_cmap('rainbow')
    rnbw = cm = plt.get_cmap('RdBu')
    rnbw = cm = plt.get_cmap('coolwarm')
    cNorm  = colors.Normalize(vmin=vmin, vmax=vmax)
    scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=rnbw)
    scalarMap.set_array(vals)
    
    colorVal = scalarMap.to_rgba(vals)
    
    title = source + ' ' + CDATE +', assimilated'
    
    
    fig = plt.figure(figsize=(12,9))
    ax = fig.add_subplot(1, 1, 1,
                         projection=ccrs.PlateCarree(),
                         title=title)
#    ax.set_extent([0, 360, -90, 90])
    ax.set_extent([-180, 180, -90, 90 ])
    ax.scatter(lon, lat,c=colorVal, marker='.',s=10)
    #ax.set_title(title)
    ax.coastlines()
    ax.gridlines()



