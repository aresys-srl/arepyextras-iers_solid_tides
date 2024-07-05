# Copyright (C) 2024 Aresys S.r.l.

add_library(solid
    SHARED
    solid_core.for
    solid.f90)

target_include_directories(solid
    INTERFACE
    $<BUILD_INTERFACE:${CMAKE_SOURCE_DIR}/include>
    $<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}>)

target_compile_options(solid
    PRIVATE
    $<$<AND:$<PLATFORM_ID:Linux>,$<AND:$<COMPILE_LANGUAGE:Fortran>,$<Fortran_COMPILER_ID:GNU>>>:-std=legacy -fno-automatic>
    $<$<AND:$<PLATFORM_ID:Linux>,$<AND:$<COMPILE_LANGUAGE:Fortran>,$<Fortran_COMPILER_ID:IntelLLVM>>>:-nostand -save -fp-model=precise>
    $<$<AND:$<PLATFORM_ID:Windows>,$<AND:$<COMPILE_LANGUAGE:Fortran>,$<Fortran_COMPILER_ID:IntelLLVM>>>:/nostand /Qsave /fp:precise>)

install(TARGETS solid
    LIBRARY
        DESTINATION ${CMAKE_INSTALL_LIBDIR}
        COMPONENT Runtime
    RUNTIME
        DESTINATION ${CMAKE_INSTALL_BINDIR}
        COMPONENT Runtime)

