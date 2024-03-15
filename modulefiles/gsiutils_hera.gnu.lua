help([[
]])

prepend_path("MODULEPATH", "/scratch1/NCEPDEV/nems/role.epic/spack-stack/spack-stack-1.6.0/envs/gsi-addon-dev/install/modulefiles/Core")
--Needed for openmpi build
prepend_path("MODULEPATH", "/scratch1/NCEPDEV/jcsda/jedipara/spack-stack/modulefiles")

local python_ver=os.getenv("python_ver") or "3.11.6"
local stack_intel_ver=os.getenv("stack_gcc_ver") or "9.2.0"
local stack_impi_ver=os.getenv("stack_openmpi_ver") or "4.1.5"
local cmake_ver=os.getenv("cmake_ver") or "3.23.1"
local openblas_ver=os.getenv("cmake_ver") or "0.3.24"

load(pathJoin("stack-gcc", stack_gcc_ver))
load(pathJoin("stack-openmpi", stack_openmpi_ver))
load(pathJoin("python", python_ver))
load(pathJoin("cmake", cmake_ver))

load("gsiutils_common")

load(pathJoin("prod_util", prod_util_ver))
load(pathJoin("openblas", openblas_ver))

whatis("Description: GSI utilities environment on Hera with GNU Compilers")
