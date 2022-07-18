#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 14:27:30 2021

@author: mossland
"""

#import osense_old
import osense
import pandas as pd
import pickle
import datetime
import os.path

#exp='desert'
#exp='narwal'
#exp='carrot'
#exp='vassal'
#exp='wombat'
exp='rodeo'
#datadir = '/Users/mossland/Desktop/work/EFSOI/carrot/' 
#datadir='/work/noaa/stmp/aeichman/comrot/carrot/osense/'
datadir='/work2/noaa/stmp/aeichman/comrot/' + exp + '/osense/'
#datadir='/work/noaa/stmp/aeichman/comrot/' + exp + '/osense/'

#cycleinit = datetime.datetime( 2021, 6, 9, 12 )
#cycleend = datetime.datetime( 2021, 6, 11, 0 )
cycleinit = datetime.datetime( 2020, 12,14, 12 )
#cycleend = datetime.datetime( 2020, 12, 17, 12 )
#cycleinit = datetime.datetime( 2020, 12,17, 18 )
cycleend = datetime.datetime( 2021, 1, 12, 18 )
#cycleinit= datetime.datetime( 2021, 1, 9, 12 )
#cycleend= datetime.datetime( 2021, 1, 12, 18 )

# these are sensors to consolidate across plaforms
sensors = ['airs','amsr','amsua','atms','avhrr','cris','iasi','mhs','saphir','seviri','ssmis']

# these probably shouldn't be changed
cycledelta = datetime.timedelta( hours = 6 )




thiscycle = cycleinit
while thiscycle <= cycleend:
    
    CDATE = thiscycle.strftime("%Y%m%d%H")
    PDY = thiscycle.strftime("%Y%m%d")
    cyc = thiscycle.strftime("%H")

    
    filename = 'osense_' + CDATE + '_final.dat'

    if not os.path.isfile(datadir + filename):
           print('skipping ' + datadir + filename)
           thiscycle += cycledelta
           continue
        
    #( convdata, satdata )= osense.read_osense('osense_2017091000.dat')
    ( convdata, satdata, idate )= osense.read_osense(datadir + filename)
 
    print(convdata['assimilated'].value_counts()) 
    print(satdata['assimilated'].value_counts() )
    
    satdata = satdata[satdata['assimilated'] == 1 ]  
    convdata = convdata[convdata['assimilated'] == 1 ] 

    # creates a DataFrame with the mean of each satellite instrument
    #meanbyobtype = satdata.groupby('obtype').mean()
    
    for sensor in sensors:
        mask = satdata.obtype.str.contains(sensor)
        satdata.loc[mask,'obtype'] = sensor.upper()
    
    
    satmeanbyobtype=satdata[['obtype','osense_kin','osense_dry','osense_moist']].groupby('obtype').mean()
    #cmeanbyobtype=convdata[['stattype','osense_kin','osense_dry','osense_moist']].groupby('stattype').mean()
    
    
    convcodes = pd.read_csv('convdata_codes.csv')
    
    # associate each data point with its source, by code
    # it would be more efficient to take the mean of the observation sensitivities by
    # code/stattype, but this way the mean is by the message column in the codes
    # (ADPUPA, AIRCRAFT, etc) to consolidate for simpler graphing. Taking the mean 
    # by code/stattype would break it down by data source more
    convbycodes=pd.merge(convdata,convcodes,how='left',left_on='stattype', right_on='code')
    
    # drop message='NA'/message02='Empty'
    indices=convbycodes[convbycodes['message02']=='Empty'].index
    convbycodes.drop(indices,inplace = True)
 
    #convgrouping='message02'
    convgrouping='message'
  
    convmeanbymsg2=convbycodes[[convgrouping,'osense_kin','osense_dry','osense_moist']].groupby(convgrouping).mean()
    
    meanimpacts=pd.concat([satmeanbyobtype,convmeanbymsg2])
    
    
    satsumbyobtype=satdata[['obtype','osense_kin','osense_dry','osense_moist']].groupby('obtype').sum()
    convsumbymsg2=convbycodes[[convgrouping,'osense_kin','osense_dry','osense_moist']].groupby(convgrouping).sum()
    
    sumimpacts=pd.concat([satsumbyobtype,convsumbymsg2])
    
    
    satcntbyobtype=satdata[['obtype','osense_kin','osense_dry','osense_moist']].groupby('obtype').count()
    convcntbymsg2=convbycodes[[convgrouping,'osense_kin','osense_dry','osense_moist']].groupby(convgrouping).count()
    cntimpacts=pd.concat([satcntbyobtype,convcntbymsg2])
    
    moist = pd.concat([cntimpacts['osense_moist'],sumimpacts['osense_moist'],meanimpacts['osense_moist']], axis=1 )
    moist.columns =  ['count', 'sum','mean']
    dry = pd.concat([cntimpacts['osense_dry'],sumimpacts['osense_dry'],meanimpacts['osense_dry']], axis=1 )
    dry.columns =  ['count', 'sum','mean']
    kin = pd.concat([cntimpacts['osense_kin'],sumimpacts['osense_kin'],meanimpacts['osense_kin']], axis=1 )
    kin.columns =  ['count', 'sum','mean']
    
    
    
    
    
    
    outfilename = 'stat_' + CDATE + '.pkl'
    #outfile = open('./pickle2/'+ outfilename,'wb')
    outfile = open('./' + exp + '/'+ outfilename,'wb')
    pickle.dump([moist,dry,kin],outfile)
    outfile.close()

    thiscycle += cycledelta




