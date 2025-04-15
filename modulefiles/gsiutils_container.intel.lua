help([[
]])

prepend_path("MODULEPATH", "/opt/spack-stack/spack-stack-1.6.0/envs/unified-env/install/modulefiles/Core")
prepend_path("MODULEPATH", "/opt/spack-stack/spack-stack-1.6.0/envs/unified-env/install/modulefiles/intel-oneapi-mpi/2021.9.0/intel/2021.10.0")
prepend_path("MODULEPATH", "/opt/spack-stack/spack-stack-1.6.0/envs/unified-env/install/modulefiles/intel/2021.10.0")

--local python_ver=os.getenv("python_ver") or "3.10.2"
local stack_intel_ver=os.getenv("stack_intel_ver") or "2021.10.0"
local stack_impi_ver=os.getenv("stack_impi_ver") or "2021.9.0"
local cmake_ver=os.getenv("cmake_ver") or "3.23.1"
local prod_util_ver=os.getenv("prod_util_ver") or "2.1.1"

load(pathJoin("stack-intel", stack_intel_ver))
load(pathJoin("stack-intel-oneapi-mpi", stack_impi_ver))
load(pathJoin("cmake", cmake_ver))

load("gsiutils_common")

load(pathJoin("prod_util", prod_util_ver))

pushenv("CFLAGS", "-march=ivybridge")
pushenv("FFLAGS", "-march=ivybridge")

whatis("Description: GSI utilities environment in a container with Intel Compilers")
