if(BUILD_UTIL_AERODA)
  add_subdirectory(AeroDA)
endif()

if(BUILD_UTIL_COV_CALC)
  add_subdirectory(Correlated_Obs)
endif()

if(BUILD_UTIL_EFSOI)
  add_subdirectory(EFSOI_Utilities)
endif()

if(BUILD_UTIL_ENKF_GFS OR BUILD_UTIL_ENKF_ARW)
  add_subdirectory(EnKF)
endif()

if(BUILD_UTIL_NCIO)
  add_subdirectory(netcdf_io)
endif()

if(BUILD_UTIL_COM)
  add_subdirectory(Analysis_Utilities)
  add_subdirectory(bufr_tools)
  add_subdirectory(radar_process)
endif()

if(BUILD_UTIL_BKGERR)
  add_subdirectory(NMC_Bkerror)
endif()

if(BUILD_UTIL_ETC)
  add_subdirectory(FOV_utilities)
  add_subdirectory(Single_Observation)
  add_subdirectory(zero_biascoeff)
endif()

# These utilities do not have CMake builds and are unlikely used or usable
#add_subdirectory(Config)
#add_subdirectory(GEN_BE_V2.0)
#add_subdirectory(GMI_BUFR_gen)
#add_subdirectory(Misc)
#add_subdirectory(MODIS_AOD)
#add_subdirectory(NCEP_bkerror)
#add_subdirectory(NCEPgsi_Coupler)
#add_subdirectory(Radiance_bias_correction_Utilities)
#add_subdirectory(Radiance_Utilities)
