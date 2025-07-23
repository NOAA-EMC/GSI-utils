help([[
]])

prepend_path("MODULEPATH", "/opt/spack-stack/spack-stack-1.6.0/envs/unified-env/install/modulefiles/Core")
prepend_path("MODULEPATH", "/opt/spack-stack/spack-stack-1.6.0/envs/unified-env/install/modulefiles/intel-oneapi-mpi/2021.9.0/intel/2021.10.0")
prepend_path("MODULEPATH", "/opt/spack-stack/spack-stack-1.6.0/envs/unified-env/install/modulefiles/intel/2021.10.0")

stack_intel_ver=os.getenv("stack_intel_ver") or "2021.10.0"
stack_impi_ver=os.getenv("stack_impi_ver") or "2021.9.0"

load("gnu")
load(pathJoin("stack-intel", stack_intel_ver))
load(pathJoin("stack-intel-oneapi-mpi", stack_impi_ver))
unload("gnu")

setenv("cmake_ver", "3.23.1")
setenv("ip_ver", "4.3.0")
setenv("bufr_ver", "12.0.1")
setenv("sigio_ver", "2.3.2")
setenv("sfcio_ver", "1.4.1")
setenv("ncio_ver", "1.1.2")
setenv("ncdiag_ver", "1.1.2")

load("gsiutils_common")

local prod_util_ver=os.getenv("prod_util_ver") or "2.1.1"
load(pathJoin("prod_util", prod_util_ver))

pushenv("CFLAGS", "-march=ivybridge")
pushenv("FFLAGS", "-march=ivybridge")

whatis("Description: GSI utilities environment in a container with Intel Compilers")
