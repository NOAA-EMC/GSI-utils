help([[
]])

prepend_path("MODULEPATH", "/opt/spack-stack/spack-stack-1.9.2/envs/unified-env/install/modulefiles/Core")

stack_oneapi_ver=os.getenv("stack_oneapi_ver") or "2024.2.0"
stack_impi_ver=os.getenv("stack_impi_ver") or "2021.13"

load(pathJoin("stack-oneapi", stack_oneapi_ver))
load(pathJoin("stack-intel-oneapi-mpi", stack_impi_ver))

load("gsiutils_common")

local prod_util_ver=os.getenv("prod_util_ver") or "2.1.1"
load(pathJoin("prod_util", prod_util_ver))

pushenv("CFLAGS", "-march=ivybridge")
pushenv("FFLAGS", "-march=ivybridge")

whatis("Description: GSI utilities environment in a container with Intel Compilers")
