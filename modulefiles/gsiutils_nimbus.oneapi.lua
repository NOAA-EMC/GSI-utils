help([[
]])

prepend_path("MODULEPATH", "/lfs/work/alexander_richert/stack/spack-stack/envs/g2-3.4.5-oneapi-2026.1.0-addon/modules_flat/Core")

local netcdf_c_ver=os.getenv("netcdf_c_ver") or "4.9.2"
local netcdf_fortran_ver=os.getenv("netcdf_fortran_ver") or "4.6.1"
local bacio_ver=os.getenv("bacio_ver") or "2.4.1"
local w3emc_ver=os.getenv("w3emc_ver") or "2.13.0"
local ncdiag_ver=os.getenv("ncdiag_ver") or "1.1.3"
local cmake_ver=os.getenv("cmake_ver") or "3.31.11"
local python_ver=os.getenv("python_ver") or "3.11.15"
local python_venv_ver=os.getenv("python_venv_ver") or "1.0"
local py_setuptools_ver=os.getenv("py_setuptools_ver") or "73.0.1"
local py_numpy_ver=os.getenv("py_numpy_ver") or "1.26.4"
local bufr_ver=os.getenv("bufr_ver") or "12.3.0"
local ip_ver=os.getenv("ip_ver") or "5.4.0"
local sigio_ver=os.getenv("sigio_ver") or "2.3.3"
local sfcio_ver=os.getenv("sfcio_ver") or "1.4.2"
local nemsio_ver=os.getenv("nemsio_ver") or "2.5.5"
local wrf_io_ver=os.getenv("wrf_io_ver") or "1.3.0"
local ncio_ver=os.getenv("ncio_ver") or "1.1.2"
local crtm_ver=os.getenv("crtm_ver") or "2.4.0.1"
local openblas_ver=os.getenv("openblas_ver") or "0.3.33"

load(pathJoin("cmake", cmake_ver))
load(pathJoin("netcdf-c", netcdf_c_ver))
load(pathJoin("netcdf-fortran", netcdf_fortran_ver))

load(pathJoin("python", python_ver)) 
load(pathJoin("python-venv", python_venv_ver))
load(pathJoin("py-setuptools", py_setuptools_ver))
load(pathJoin("py-numpy", py_numpy_ver))
load(pathJoin("bufr", bufr_ver))
load(pathJoin("bacio", bacio_ver))
load(pathJoin("w3emc", w3emc_ver))
load(pathJoin("ip", ip_ver))
load(pathJoin("sigio", sigio_ver))
load(pathJoin("sfcio", sfcio_ver))
load(pathJoin("nemsio", nemsio_ver))
load(pathJoin("wrf-io", wrf_io_ver))
load(pathJoin("ncio", ncio_ver))
load(pathJoin("gsi-ncdiag", ncdiag_ver))
load(pathJoin("openblas", openblas_ver))

-- Set Intel oneAPI compilers for CMake
setenv("FC", "/opt/intel/oneapi/compiler/2026.1/bin/ifx")
setenv("CC", "/opt/intel/oneapi/compiler/2026.1/bin/icx")
setenv("CXX", "/opt/intel/oneapi/compiler/2026.1/bin/icpx")

-- Restore oneAPI compiler libraries to front of LD_LIBRARY_PATH for precedence
-- Add libcilkrts from oneAPI 2023.2.1 for backwards compatibility
local oneapi_path = os.getenv("ONEAPI_LD_PATH") or ""
if oneapi_path ~= "" then
  prepend_path("LD_LIBRARY_PATH", "/opt/intel/oneapi/compiler/2023.2.1/linux/compiler/lib/intel64_lin")
  for dir in string.gmatch(oneapi_path, "[^:]+") do
    prepend_path("LD_LIBRARY_PATH", dir)
  end
end

whatis("Description: GSI utilities environment on Nimbus with Intel oneAPI Compilers")
