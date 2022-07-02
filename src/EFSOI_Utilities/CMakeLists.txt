if(NOT enkf_FOUND)
  message(WARNING "Utils: EFSOI utilities require the EnKF library and was not found")
  message(WARNING "Utils: EFSOI utilities are disabled")
  return()
endif()

if(NOT ENKF_MODE MATCHES "GFS")
  message(FATAL_ERROR "Utils: Found incompatible EnKF = ${ENKF_MODE} for EFSOI utilities")
endif()

add_subdirectory(src)
