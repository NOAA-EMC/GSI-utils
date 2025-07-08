help([[
GSI utilities environment on NOAA Cloud with Intel Compilers
]])

prepend_path("MODULEPATH", "/contrib/spack-stack-rocky8/spack-stack-1.9.2/envs/ue-oneapi-2024.2.1/install/modulefiles/Core")
prepend_path("MODULEPATH", "/apps/modules/modulefiles")

local gcc_ver=os.getenv("gcc_ver") or "13.2.0"
local stack_oneapi_ver=os.getenv("stack_oneapi_ver") or "2024.2.1"
local stack_intel_oneapi_mpi_ver=os.getenv("stack_intel_oneapi_mpi_ver") or "2021.13"
local python_ver=os.getenv("python_ver") or "3.11.7"
local prod_util_ver=os.getenv("prod_util_ver") or "2.1.1"

load(pathJoin("gnu", gcc_ver))
load(pathJoin("stack-oneapi", stack_oneapi_ver))
load(pathJoin("stack-intel-oneapi-mpi", stack_intel_oneapi_mpi_ver))
load(pathJoin("python", python_ver))
load(pathJoin("prod_util", prod_util_ver))

load("gsiutils_common")

pushenv("CFLAGS", "-xHOST")
pushenv("FFLAGS", "-xHOST")

whatis("Description: GSI utilities environment on NOAA Cloud with Intel Compilers")
