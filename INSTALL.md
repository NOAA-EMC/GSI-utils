## Build and Install Instructions
---

### Prerequisites
A supported Fortran compiler (see table below).  Other versions may work, in particular if close to the versions listed below.

| Compiler vendor | Supported (tested) versions                                |
|-----------------|------------------------------------------------------------|
| Intel           | 18.0.3.222 and above                                       |
| GNU             | 10.3.0 and above                                           |

A supported MPI library (see table below).  Other versions may work, in particular if close to the versions listed below.

| MPI library     | Supported (tested) versions                                |
|-----------------|------------------------------------------------------------|
| MPICH           | 3.3.1 and above                                            |
| Open MPI        | 3.1.5 and above                                            |
| Intel MPI       | 2018.0.4 and above                                         |

Third-party libraries (TPL) compiled with the same compiler and MPI library (where applicable).

| Library         | Supported (tested) versions                                |
|-----------------|------------------------------------------------------------|
| CMake           | 3.20.1 and above                                           |
| HDF5            | 1.10.4 and above                                           |
| NetCDF-C        | 4.7.3 and above                                            |
| NetCDF-Fortran  | 4.5.2 and above                                            |

NCEP Libraries (NCEPLibs) compiled with the same compiler and MPI library (where applicable).

| Library         | Supported (tested) versions                                |
|-----------------|------------------------------------------------------------|
| BUFR            | 11.6.0 and above                                           |
| IP              | 3.3.3 and above                                            |
| SP              | 2.3.3 and above                                            |
| BACIO           | 2.4.1 and above                                            |
| W3EMC           | 2.9.1 and above                                            |
| SIGIO           | 2.3.2 and above                                            |
| SFCIO           | 1.4.1 and above                                            |
| NEMSIO          | 2.5.2 and above                                            |
| NCIO            | 1.1.2 and above                                            |
| WRF_IO          | 1.2.0 and above                                            |
| CRTM            | 2.3.0 and above                                            |

Optional Libraries
| Library         | Supported (tested) versions                                |
|-----------------|------------------------------------------------------------|
| GSI-ncdiag      | 1.0.0 and above (used for Correlated obs. error.)          |
| GSI (Regional)  | EnKF ARW utilities                                         |
| EnKF (GFS)      | EFSOI utilities                                            |

### Building the GSI Utilities

`CMake` employs an out-of-source build.  Create a directory for configuring the build and cd into it:

```bash
mkdir -p build && cd build
```

Set the compilers, if needed, to match those being used for compiling the TPL and NCEPLibs listed above: `FC` environment variable can be used to point to the desired Fortran compiler.

Execute `cmake` from inside your build directory.

```bash
cmake -DCMAKE_INSTALL_PREFIX=<install-prefix> <CMAKE_OPTIONS> /path/to/GSI-utils-source
```

If the dependencies are not located in a path recognized by `cmake` e.g. `/usr/local`, it may be necessary to provide the appropriate environment variables e.g. `<package_ROOT>` or `CMAKE_PREFIX_PATH` so that `cmake` is able to locate these dependencies.

`gsi_ROOT` and `enkf_ROOT` provides the path to the `GSI` and `EnKF` installations on the system.  Refer to the installation instructions for the GSI/EnKF [here](https://github.com/NOAA-EMC/GSI/blob/develop/INSTALL.md)

The installation prefix for GSI-utils tools is provided by the `cmake` command-line argument `-DCMAKE_INSTALL_PREFIX=<install-prefix>`

To build and install:

```
make -j<x>
make install
```

### CMake Options

CMake allows for various options that can be specified on the command line via `-DCMAKE_OPTION=VALUE` or from within the ccmake gui. The list of options currently available is as follows:

| Option                | Description (Default)                                |
|-----------------------|------------------------------------------------------|
| `BUILD_UTIL_ALL`      | Build All Utilities (`OFF`)                          |
| `BUILD_UTIL_AERODA`   | Build Aerosol DA utility (`OFF`)                     |
| `BUILD_UTIL_COV_CALC` | Build Correlated Obs. Error utility (`OFF`)          |
| `BUILD_UTIL_EFSOI`    | Build Ensemble FSOI application (`OFF`)              |
| `BUILD_UTIL_ENKF_GFS` | Build GFS ensemble utilities (`OFF`)                 |
| `BUILD_UTIL_ENKF_ARW` | Build ARW ensemble utilities (`OFF`)                 |
| `BUILD_UTIL_NCIO`     | Build NetCDF IO utilities (`OFF`)                    |
| `BUILD_UTIL_COM`      | Build Miscellaneous community utilities (`OFF`)      |
| `BUILD_UTIL_BKGERR`   | Build Background Error utility (`OFF`)               |
| `BUILD_UTIL_ETC`      | Build Miscellaneous utilities (`OFF`)                |

