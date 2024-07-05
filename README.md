# IERS 2003 Solid Earth Tides

`Arepyextras IERS Solid Tides` is the Aresys Python wrapper of fortran code to compute solid tides.

This package is a thin Python wrapper of the [`solid.for`](http://geodesyworld.github.io/SOFTS/solid.htm) code written
by Dennis Milbert (based on dehanttideinelMJD.f from V. Dehant, S. Mathews, J. Gipson and C. Bruyninx) to compute Solid
Earth Tides displacements along east, north and up directions following the official 2010 IERS Conventions definition
(section 7.1.1).

The package can be installed via pip:

```shell
pip install arepyextras-iers_solid_tides
```

> [!NOTE]  
> The SOLID precompiled libraries ``.so/.dll`` are included in this package. Nevertheless, source code for the Fortran SOLID program has been included and can be found at `arepyextras-iers_solid_tides\source`. This can be compiled following the instructions below on any platform.

## SOLID source code building instructions

### Prerequisites

- C, C++ and Fortran compilers
- CMake >= 3.14

### Build and pack steps

From the project root folder:

```bash
mkdir _build && cd _build
cmake -D CMAKE_BUILD_TYPE=Release ..
cmake --build .
cpack -G TGZ -D CPACK_COMPONENTS_ALL=Runtime -D CPACK_PACKAGE_FILE_NAME="solidtools-dynamic-release"
tar -xzvf solidtools-dynamic-release-Runtime.tar.gz
```

The compiled shared library is available under
`./solidtools-dynamic-release/lib`

Decompress the archive to access the compiled library ``.dll/.so`` and copy the file to the `arepyextras-iers_solid_tides/arepyextras/iers_solid_tides/resources` path, replacing the older file.
