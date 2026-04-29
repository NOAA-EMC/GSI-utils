help([[
GSI utilities environment on AWS ec2 with Intel Compilers
]])

prepend_path("MODULEPATH", "/opt/spack-stack/envs/ue-oneapi-2024.2.1/install/modulefiles/Core")
prepend_path("MODULEPATH", "/opt/modulefiles")

stack_oneapi_ver=os.getenv("stack_oneapi_ver") or "2024.2.1"
stack_impi_ver=os.getenv("stack_impi_ver") or "2021.13"
cmake_ver=os.getenv("cmake_ver") or "3.27.9"

load(pathJoin("stack-oneapi", stack_oneapi_ver))
load(pathJoin("stack-intel-oneapi-mpi", stack_impi_ver))
load(pathJoin("cmake", cmake_ver))

load("gsiutils_common")

pushenv("CFLAGS", "-xHOST")
pushenv("FFLAGS", "-xHOST")

whatis("Description: GSI utilities environment on AWS ec2 with Intel Compilers")
