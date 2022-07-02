# No utility code here depends on the GSI library
if(BUILD_UTIL_ENKF_GFS)
  add_subdirectory(gfs)
endif()

# Utility code here depends on the GSI library
# Specifically GSI_MODE=Regional
if(BUILD_UTIL_ENKF_ARW)
  if(NOT gsi_FOUND)
    message(WARNING "Utils: EnKF ARW utilities require the GSI library and was not found")
    message(WARNING "Utils: EnKF ARW utilities are disabled")
    return()
  endif()

  if(NOT GSI_MODE MATCHES "Regional")
    message(FATAL_ERROR "Utils: Found incompatible GSI = ${GSI_MODE} for EnKF ARW utilities")
  endif()
  add_subdirectory(arw)
endif()
