####################################################################
# FLAGS COMMON TO ALL BUILD TYPES
####################################################################

set(CMAKE_Fortran_FLAGS "${CMAKE_Fortran_FLAGS} -g -traceback -implicitnone")

####################################################################
# RELEASE FLAGS
####################################################################

set(CMAKE_Fortran_FLAGS_RELEASE "-O3")

####################################################################
# DEBUG FLAGS
####################################################################

set(CMAKE_Fortran_FLAGS_DEBUG "-O0 -fp-model=source -debug -ftrapuv -warn all,nointerfaces -check all,noarg_temp_created -fstack-protector")

####################################################################
# LINK FLAGS
####################################################################

set(CMAKE_Fortran_LINK_FLAGS "")

####################################################################
# FLAGS FOR AUTOPROFILING
####################################################################

set(Fortran_AUTOPROFILING_FLAGS "-finstrument-functions")

####################################################################

# Meaning of flags
# ----------------
# -g                     : Generate symbolic debug information
# -traceback             : Generate extra info for traceback on runtime error
# -implicitnone          : No implicit typing allowed
# -O3                    : Aggressive optimization
# -O0                    : No optimization
# -fp-model=source       : Floating point model (use = for oneAPI, space for Classic)
# -debug                 : Enable debug mode
# -ftrapuv               : Initialize stack local variables to unusual values
# -warn all,nointerfaces : Enable all warnings except interfaces
# -check all,noarg_temp_created : Enable runtime checks
# -fstack-protector      : Enable stack protection
# -finstrument-functions : Enable function instrumentation for profiling
#
# Note: IntelLLVM (oneAPI) uses -fp-model=source (with =) while
#       Intel Classic uses -fp-model source (with space)
