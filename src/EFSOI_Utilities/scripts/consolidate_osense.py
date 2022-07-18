#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import osense
import pandas as pd
import pickle
import datetime
import os.path

exp='rodeo'
#exp='baily'

#datadir='/work2/noaa/stmp/aeichman/comrot/' + exp + '/osense/'
#datadir='/work/noaa/stmp/aeichman/comrot/' + exp + '/osense/'
#rootdir = '/Users/mossland/Desktop/work/EFSOI/' + exp 
rootdir = '/work/noaa/da/aeichman/gsidev/EFSOI-dev-post/GSI/util/EFSOI_Utilities/scripts/' + exp
indir = '/work2/noaa/stmp/aeichman/comrot/rodeo/osense/'
outdir = rootdir + '/consolidated/'

# baily
cycleinit = datetime.datetime( 2021, 12,10, 0 )
cycleend = datetime.datetime( 2021, 12, 14, 18 )

# rodeo
cycleinit = datetime.datetime( 2020, 12,14, 12 )
cycleinit = datetime.datetime( 2020, 12,14, 18 )
#cycleend = datetime.datetime( 2021, 1, 13, 18 )


# The following determines whether the conventional data points are aggregated
# by the column in convdata_codes.cvs "message02" (DETAILED = False ) or "message"
# (DETAILED = True). Generally message offers finer distinctions between the
# sources, though these are somewhat arbitrary. See convdata_codes.csv
DETAILED = True

# these are satellite sensors to consolidate across plaforms
sensors = ['airs',
           'amsr',
           'amsua',
           'atms',
           'avhrr',
           'cris',
           'iasi',
           'mhs',
           'saphir',
           'seviri',
           'ssmis']

# these are fields in the osense files and can be expanded or reduced
osensefields = ['source',
                'detailed_source',
                'indxsat',
                'osense_kin',
                'osense_dry',
                'osense_moist',
                'assimilated',
                'lat',
                'lon',
                'pres']

# time between cycles
cycles = pd.date_range( cycleinit, cycleend, freq='6H' )


for thiscycle in cycles:
    
    CDATE = thiscycle.strftime("%Y%m%d%H")
    PDY = thiscycle.strftime("%Y%m%d")
    cyc = thiscycle.strftime("%H")
    
    filename = indir + 'osense_' + CDATE + '_final.dat'

    if not os.path.isfile(filename):
           print('skipping ' + filename)
           continue
        
    ( convdata, satdata, idate )= osense.read_osense( filename )
 
    satdata['detailed_source'] = satdata['obtype']  
    satdata['source'] = satdata['obtype']  

    for sensor in sensors:
        mask = satdata.source.str.contains(sensor)
        satdata.loc[mask,'source'] = sensor.upper()
    

    # now consolidate conventional data
    
    convcodes = pd.read_csv('convdata_codes.csv')

    # associate each data point with its source, by code
    # this also effectively adds the columns 'source' and 'detailed_source'
    convbycodes=pd.merge(convdata,convcodes,how='left',
                         left_on='stattype', 
                         right_on='code')
    
    # drop message='NA'/message02='Empty'
    # data not dumped/not used
    indices=convbycodes[convbycodes['source']=='Empty'].index
    convbycodes.drop(indices,inplace = True)
    
    # some stattypes, namely 700, have no corresponding code, and so have
    # nans in the code, source, and detailed_source fields. This replaces those
    # fields with the stattype
    nanmask = convbycodes.code.isna()
    nanstattypes = convbycodes.loc[nanmask,['stattype']]
    for nanstattype in nanstattypes.stattype.unique():
        convbycodes.loc[convbycodes['stattype'] == nanstattype, \
                        ['source','detailed_source']] = nanstattype

    
    osensedata = pd.concat([ satdata[osensefields], convbycodes[osensefields] ] )
    
    
    outfilename = outdir + 'osense_' + CDATE + '.pkl'
    outfile = open( outfilename, 'wb' )
    pickle.dump([ idate, osensedata ], outfile )
    outfile.close()



