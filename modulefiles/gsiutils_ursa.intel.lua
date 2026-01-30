help([[
]])

prepend_path("MODULEPATH", "/contrib/spack-stack/spack-stack-2.0.0/envs/ue-oneapi-2025.2.1/modules/Core")

local stack_oneapi_ver=os.getenv("stack_oneapi_ver") or "2025.2.1"
local stack_impi_ver=os.getenv("stack_impi_ver") or "2021.13"
local oneapi_mkl_ver=os.getenv("oneapi_mkl_ver") or "2025.2.0"
local cmake_ver=os.getenv("cmake_ver") or "3.31.8"
local crtm_fix_ver=os.getenv("crtm_fix_ver") or "2.4.0.2"

load(pathJoin("stack-intel-oneapi-compilers", stack_oneapi_ver))
load(pathJoin("stack-intel-oneapi-mpi", stack_impi_ver))
load(pathJoin("intel-oneapi-mkl", oneapi_mkl_ver))
load(pathJoin("cmake", cmake_ver))

load("gsiutils_common")

whatis("Description: GSI Utilities environment on Ursa with Intel Compilers")
