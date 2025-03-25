help([[
]])

prepend_path("MODULEPATH", "/opt/spack-stack/spack-stack-1.8.0/envs/unified-env/install/modulefiles/Core")

--local python_ver=os.getenv("python_ver") or "3.11.6"
local stack_intel_ver=os.getenv("stack_intel_ver") or "2021.10.0"
local stack_impi_ver=os.getenv("stack_impi_ver") or "2021.12.2"
local cmake_ver=os.getenv("cmake_ver") or "3.27.9"
local prod_util_ver=os.getenv("prod_util_ver") or "2.1.1"

load(pathJoin("stack-intel", stack_intel_ver))
load(pathJoin("stack-intel-oneapi-mpi", stack_impi_ver))
load(pathJoin("cmake", cmake_ver))

load("gsiutils_common")

load(pathJoin("prod_util", prod_util_ver))

pushenv("CFLAGS", "-march=ivybridge")
pushenv("FFLAGS", "-march=ivybridge")

whatis("Description: GSI utilities environment in a container with Intel Compilers")
