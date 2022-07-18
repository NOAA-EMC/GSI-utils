from netCDF4 import Dataset    # Note: python is case-sensitive!
import netCDF4 as nc
import numpy as np
import osense

# this is determined in the observation sensitivty module in the enkf code - better would
# be to set it dynamically from the the maximum string length
strlen=20
#osensefile='/scratch1/NCEPDEV/stmp4/Andrew.Eichmann/testtest/osense/osense_2019111918_final.dat'
dir='/work2/noaa/stmp/aeichman/comrot/EFOSIsandbox/osense/'
filename='osense_2020122418_final.dat'
osensefile=dir+filename

columns = [ ( 'obfit_prior' , 'Observation fit to the first guess'),
	( 'obsprd_prior' , 'Spread of observation prior'),
	( 'ensmean_obnobc' , 'Ensemble mean first guess (no bias correction)'),
	( 'ensmean_ob' , 'Ensemble mean first guess (bias corrected)'),
	( 'ob' , 'Observation value'),
	( 'oberrvar' , 'Observation error variance'),
	( 'lon' , 'Longitude'),
	( 'lat' , 'Latitude'),
	( 'pres' , 'Pressure'),
	( 'time' , 'Observation time'),
	( 'oberrvar_orig' , 'Original error variance'),
	( 'osense_kin' , 'Observation sensitivity (kinetic energy) [J/kg]'),
	( 'osense_dry' , 'Observation sensitivity (Dry total energy) [J/kg]'),
	( 'osense_moist' , 'Observation sensitivity (Moist total energy) [J/kg]') ]

(convdata, satdata, idate )= osense.read_osense( osensefile)




def fill_nc( dataset, ncfilname ):


   obnum_in = dataset.shape[0] 
   try: ncfile.close()  # just to be safe, make sure dataset is not already open.
   except: pass
   ncfile = Dataset(ncfilename,mode='w',format='NETCDF4') 

   _ = ncfile.createDimension('nobs', obnum_in) 
   _ = ncfile.createDimension('nchars',strlen)

   for dim in ncfile.dimensions.items():
       print(dim)

   nobs = ncfile.createVariable('nobs', np.int32, ('nobs',))
   nobs.long_name = 'number of observations'
   nobs[:] = list(range(1,obnum_in+1))

   # netcdf isn't crazy about strings as data, so there's this
   obtype = ncfile.createVariable('obtype', 'S1', ('nobs','nchars'))
   obtypestr=np.array(dataset[ 'obtype' ],dtype='S20')    
   obtype[:] = nc.stringtochar(obtypestr )   
   obtype.long_name = 'Observation element / Platform, instrument '

   stattype = ncfile.createVariable('stattype', np.int32, ('nobs'))
   stattype.long_name = 'Conventional PREPBUFR code/Observation type'
   stattype[:] = dataset[ 'stattype' ].to_numpy()

   indxsat = ncfile.createVariable('indxsat', np.int32, ('nobs'))
   indxsat.long_name = 'Satellite index (channel) set to zero'
   indxsat[:] = dataset[ 'indxsat' ].to_numpy()

   for column in columns:
       
       varname = column[0]
       ncvar = ncfile.createVariable(varname, np.float32, ('nobs'))
       ncvar.long_name = column[1]
       ncvar[:] = dataset[ varname ].to_numpy()
  
   return ncfile


ncfilename = 'osense_' + str(idate) + '_sat.nc'
ncfile = fill_nc( satdata, ncfilename )
ncfile.title='My satellite osense data'
print(ncfile)
ncfile.close(); print('Dataset is closed!')

ncfilename = 'osense_' + str(idate) + '_conv.nc'
ncfile = fill_nc( convdata, ncfilename )
ncfile.title='My conventional and ozone osense data'
print(ncfile)
ncfile.close(); print('Dataset is closed!')


